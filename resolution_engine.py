from tkinter import *
from tkinter import ttk
import pyprover as pyp
import pyparsing as pyparse

def strip_all(string):
    str2 = ""
    for letter in string:
        if not letter.isspace():
            str2 += letter
    return str2

def paren_even(string):
    num_left_exceeds = 0
    for letter in string:
        if letter == "(":
            num_left_exceeds += 1
        elif letter == ")":
            num_left_exceeds -= 1
    return num_left_exceeds == 0

def remove_outer_parens(string):
    if len(string) > 1 and string[0] == "(" and string[len(string) - 1] == ")":
        return string[1:len(string)-1]
    elif len(string) > 1 and string[0] == "{" and string[len(string) - 1] == "}":
        return string[1:len(string)-1]
    return string

class ResolutionEngine(ttk.Frame):
    def __init__(self, master, app, **kwargs):
        # initialize the frame
        super().__init__(master, **kwargs)

        # useful variables
        self.app = app      # the parent app

    def verify_all(self):
        premise_listbox = self.app.leftframe.plist
        conclusion_listbox = self.app.leftframe.clist
        plist_exps = list()

        premises_OR = dict() # this is actually useful for "step 2"
        concl_OR = list()

        # parse all premises
        if premise_listbox.size() < 1:
            print("ERROR: no premises")
            return
        
        for i in range(premise_listbox.size()):
            #print("Premise " + str(i) + ": " + str(premise_listbox.get(i)))
            try:
                this_exp = pyp.expr(premise_listbox.get(i).upper())

                pstr = str(i)
                this_lis = list()
                for part in premise_listbox.get(i).split("&"):
                    part = strip_all(part)
                    if paren_even(part):
                        #premises_OR.append(remove_outer_parens(part))
                        #premises_OR[pstr] = remove_outer_parens(part)
                        this_lis.append(remove_outer_parens(part).upper())
                    else:
                        print("ERROR: premise '" + str(premise_listbox.get(i))
                              + "' is not in CNF!")
                        return
                premises_OR[pstr] = this_lis
                
                plist_exps.append(this_exp)
            except pyparse.ParseException:
                print("ERROR: could not parse '" + str(premise_listbox.get(i))
                      + "'")
                ## INCOMP! Need to show verification failed in GUI
                return

        # parse the conclusion
        try:
            if str(conclusion_listbox.get(0)) == "Conclusion":
                raise pyparse.ParseException("conclusion")
            concl_exp = pyp.expr(conclusion_listbox.get(0).upper())
            concl_neg = str(pyp.simplify(~concl_exp))
            
            for part in concl_neg.split("&"): # NEGATE conclusion parts!
                if paren_even(strip_all(part)):
                    concl_OR.append(remove_outer_parens(strip_all(part)).upper())
                else:
                    print("ERROR: conclusion does not validate to CNF!")
                    return
        except pyparse.ParseException:
            print("ERROR: could not parse '" + str(conclusion_listbox.get(0))
                  + "'")
            return

        # You might be wondering, shouldn't we invert the conclusion?
        # No! We pass it into pyprover's proves() AS-IS!

        try:
            premises_check = pyp.proves(plist_exps, concl_exp)
        except: # leave this exception generic
            print("ERROR: premises or conclusion unsound")
            return
        print("Premises and conclusion are sound: " + str(premises_check))
        ## INCOMP! Need to display in GUI

        if premises_check:
            # if premises ARE sound, then the resolution (with inverted
            # conclusion) should leave no claims "on the field"

            print("We expect (1) all verified ClauseFrames, and (2) " +
                  "a fully resolved canvas")
        else:
            # if premises do NOT match the conclusion, this doesn't mean
            # the user screwed up! It just means the resolution should
            # leave claims "on the field"
            # however, there should be no errors or unverified claims here
            # too!
            print("We expect (1) all verified ClauseFrames, and (2) " + 
                  "free attributes on the canvas")

        # great, now let's check the "top-level" clause-frames
        clause_dict = self.app.canvas.frames
        # format: {1: clause-obj-1, 2: clause-ob-2}
        # notes: currently deleting a clause doesn't update the index, so
        # there can be gaps in between clause-objs. 1, then 3, if 2 is deleted
        # and so on

        top_level = dict()
        lower_lvl = dict()

        for key in clause_dict:
            if clause_dict[key].premise_index != None:
                # top-level clauses have a premise index!
                top_level[key] = clause_dict[key]
            else:
                lower_lvl[key] = clause_dict[key]

        # great, now they're divided into two dicts
        print(top_level)
        print(lower_lvl)

        # now that we're here, we can use the premises_OR and concl_OR
        # vars that we filled out at around step 1!

        print(premises_OR)
        print(concl_OR)
        
        # step 2 formally begins: all pieces of the premises and conclusion
        # must be represented as clauses!

        for key in top_level:
            part_str = str(top_level[key].text.get()).upper()
            crop_str = remove_outer_parens(strip_all(part_str))
            matches_with = str(top_level[key].premise_index)
            print(part_str + " - " + matches_with)

            try:
                if int(matches_with) >= 0 and crop_str in premises_OR[matches_with]:
                    # TODO this possibly needs an additional check, but it
                    # might be good
                    #print("debug: '" + crop_str + "' matched")
                    premises_OR[matches_with].remove(crop_str)
                elif int(matches_with) < 0 and crop_str in concl_OR:
                    concl_OR.remove(crop_str)
                else:
                    # error triggered if clause is tagging the wrong premise
                    print("ERROR: clause '" + part_str + "' does not match "
                          + "the premise tagged")
                    return
            except KeyError:
                print("ERROR: clause '" + part_str + "' is pointing "
                      + "to a nonexistent premise")
                return

        # now we check to see if we *missed* any premises
        end_early = False
        for key in premises_OR:
            if len(premises_OR[key]) > 0:
                end_early = True
                print("ERROR: premise " + str(key) + " not represented")
        if len(concl_OR) > 0:
            end_early = True
            print("ERROR: conclusion not represented")
        if end_early:
            return

        print("debug: okay, great! all premises/conclusion represented!")

        # now we move onto step 3: verifying all lower-level claims
        # using the arrows to parent/child
        
