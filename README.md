# Fetch-Data-From-Google-Sheet-Using-Google-Sheet-API-Then-Plot-Graph
This is code for fetching the data from google sheet using google sheet API then plot the graph of that data.
Before Running this code please install gspread library using the pip command.

# pip install gspread
# pip install matplotlib
# pip install pandas

# You have to install one more module that was created by me. Name of module is:- plotgsheet.
Link of module:- https://pypi.org/project/plotgsheet/#description

# pip install plotgsheet

After installing all dependency you have to download your gspread credentials by folling these steps below.

# How to SETUP your API.
1. Go to this link given below.
   Google Developer Console: https://console.developers.google.com
2. After going there create a new project.
3. Then Activate your Google Drive and Google Sheets API.
4. Then go to Credentials --Then---> service account --Then Select(name and your role)---> Name + Role --Then Select---> Editor.
4. Then Click on KEY Then System will download and JASON File and put there where your assignment of greendeck file is an exit.
5. Then open the JASON file there will be an attribute name "client_email" copy that and click on the share button in Google Sheet and paste there that client_email and click on the send button.

# How to Run This Program.

# Important Point Whenever You Are Running This Code You Have To Connect Your System With Internet.

# You have to call this function in your code like this given below.
 gsheetplot(credentialspath,drivepath,Gtype='Line',Gtitle='Google-Sheet-Graph',Xaxis=1,Yaxis=2,AxisLabel=[1,1],PlotColor='b',savefilename='Google_Sheet_Graph')

# Whenever you will call this function in your code you have to pass some Parameters in your function.

# 1. Credentials Path.
     credentialspath="C:\\Users\\credentials.json".

# 2. Drive Path.
     drivepath='https://docs.google.com/spreadsheets/d/133jnnPzkSmrYEGfNbWaUbzJIRLhUepzM4TlB08HR-cA/edit#gid=0'

# 3. Graph Type.
     Gtype='Line' # Here is Line Chart.
     Gtype='Bar' # Here is Bar Chart.
     Gtype='Scatter' # Here is Scatter Chart.

# 4. Graph Type.
     Gtitle='G-Sheet Ploting'.

# 5. Axis Type Which Axis You Want From Your Google Sheet Columns Like....
     Xaxis=3 # XL Sheet Columns 3rd.
     Yaxis=2 # XL Sheet Columns 2rd.
     
# 6. If You Want Lables On Axis Then Pass Like This...
     AxisLabel=[0,0] # [Not X Label ,Not Y Label].
     AxisLabel=[0,1] # [Not X Label ,Y Label Yes].
     AxisLabel=[1,0] # [X Label Yes,Not Y Label].
     AxisLabel=[1,1] # [X Label Yes,Y Label Yes].

# 7. Now You Have To Pass Color Type Like This.
     PlotColor='b' # Here is Blue Color.
     PlotColor='r' # Here is Red Color.
     PlotColor='y' # Here is Yellow Color.
     PlotColor='g' # Here is Green Color.

# 8. Last Parameter You Have To Pass That is Name Of Image of Graph That Will Automatically Save.
     savefilename='Scatter' # Scatter is the name of graph that will save in your directory. 

# 9. Then System Will Final Result.


# Example of Graph Ploting From Google Sheet

1. Create a New Python File in Your Directory and Paste This Below Code in That File And Run You Will Get Result. 

    import plotgsheet # Library importing 
    
    credentialspath="C:\\Users\\credentials.json" # Path of credentials file
    
    drivepath='https://docs.google.com/spreadsheets/d/133jnnPzkSmrYEGfNbWaUbzJIRLhUepzM4TlB08HR-cA/edit#gid=0' # Drive Path
    
    plotgsheet.plotgs(credentialspath,drivepath,Gtype='Bar',Gtitle='Google-Sheet-Graph-Testing1',AxisLabel=[1,1],PlotColor='y',savefilename='PIP-Testing') # Function calling



