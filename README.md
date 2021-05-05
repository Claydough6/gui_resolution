# gui_resolution
Logical resolution application for Computability and Logic RPI course final project. Uses Tkinter library for creating the GUI and PyProver library for CNF conversion. Resolution is done locally by the resolution engine.

Authors: Clay Bell and Kevin Khaghani

## How to Use:
Note: this is found in help.txt as well. It is displayed when the help menu is clicked in the app.

How to use the application:

1. Add premises to the list with the 'Add Premise' button.
  -  you can add as many premises as you want
  -  you can only have one conclusion 

2. Delete premises by clicking on the premise then clicking the 'Delete Premise' button.

3. Edit the premises or conclusion by double clicking on the statement you want to edit.
  -  type in the new statement
  -  hit 'Enter' to save your input
  -  hit 'Escape' to stop editing without saving

4. To add clauses to the resolution screen, shift-click on an empty space to create a new statement box. 
  -  edit the text to add a clause

5. To delete a clause, select it and hit the 'delete' key.
  -  you cannot undo this as of now, so be careful

6. Clauses can be selected to modify their properties. To select a clause, click on the clause (or space around it). 
  -  it will raise up to indicate it has been selected
  -  click the clause again or anywhere else to deselect it

7. To move a clause, click the side of the clause and drag it around the screen.

8. To derive a clause from another, select the derived clause. Then select the clauses it comes from.
  -  arrows will be drawn to show the relationship.
  -  click again to undo a derivation relationship

9. To derive a top level clause from a premise statement, select a clause then click a premise to select it.
  -  this only works for clauses that aren't linked to others
  -  click the premise again to unlink it 
  -  click a different premise to change which is linked

10. To check derivations, click the 'Verify Resolution' button.
  -  this will check each premise, the conclusion, and the resolution steps
  -  any errors will be displayed in the error window
  -  if the derivation is successful the labels will change to 'valid!'

## Application Strucure:
The ResolutionGUI application consissts of a resolution engine and a graphical user interface. The GUI is used to get input from the user and display the results of the resolution. The resolution engine interacts with the GUI components to resolve the statements and clauses and check the user's derivations.

The GUI contains the following components:
 - root window (main application screen)
 - menus
 - statement and conclusion lists
 - buttons for modifying premises / verifying resolution
 - a canvas to draw the resolution
 - clasue frames on the canvas
 - separate windows displaying useful info

The root window contains all of the other graphics of the application, and is created in the main appication class ResolutionGUI.

The menus are used to access the help window and file input and output. Currently file IO is in the testing phase under the 'development' branch.

The statement and conclusion lists live in the StatementFrame class on the left side of the app. They are each instances of the EditListbox class allowing users to easily modify the premises and conclusion and add new premises.

The buttons live in the StatementFrame under the premises and conclusion. They allow users to add and delete premises as well as verify the final resolution.

The canvas is a ResolutionCanvas and controls the graphics and placement of the clause frames. Users can create, edit, delete, and move around clause frames on the canvas.

The ClauseFrame class hold the individual clause frames on the canvas and controls their properties, determining which inherit from which frames and other relevant data.

Individual window for displaying useful information to the user are created as instances of the InfoWindow class. These include the help window, error window, and success window.

