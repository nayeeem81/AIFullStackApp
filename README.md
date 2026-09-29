# AIFullStackApp

# Create the solution structure and follow the steps below to set up the AIFullStackApp in Visual Studio:

## Environment Setup

1) Install Visual Studio 2026 Community Editon from Visual Studio online web site.
2) In the Visual Studio Installer add: Python Development (Check to add  Python Web Support & Python Native Development Tools) and Node.js Development to install. 
3) Downnload and Install Node.js. Download Manually: Go directly to the official Node.js Download Page and download the LTS (Long Term Support) installer package. Node.js and npm are always installed together.
When you run the installer from the official Node.js website, npm (Node Package Manager) is completely built-in. You do not need to download or install it as a separate application.
4) Once the installer finishes running on your laptop, you can check that both are successfully installed and linked together. After install, in (win + r) cmd; command terminal write following command to check the version of node.js: 
node -v
npm -v
4) Download Olamma and install. Check that the Ollama is installed ad present in thesystem tray in the laptop.
5) Then, pull lamma3 model. Write following commands to pull and check lamma3 is running.
ollama pull llama3 (this command will pull the model, which we use for chat)
ollama run llama3 (check if the lamma3 is running. You can chat after this command.)
6) Install WSL. We will use light weight posgre sql included in the solution, we will create. Useing theDocker comose we willrunnthe image of posgres sql linux based image. Download the wsl .msi in the local laptop ad restart the laptop.Then, oenthe command prompt and run: wsl --status
7) Install Docker desktop to use as the container of the postgres sql image.

## Visual Studio Solution (two projects: frontend and backend)

8) Open Visual Studio, click File > New > Project/Solution. Select template React App (Java Script), name frontend as project name and AIFullStackApp as soluton name. Create the solution.
10) In the solution explorer, over the solution, right click; add new project. Select Python Application, name as backend.
11) In the backend project, add a new folder app. Inside the app folder, create a python file named main.py. In the backend project, add a file: requirements.txt (check the package names).
12) Right click on the Python Environments and click Add Environment. Name the environment: .venv in the textbox of the popup window of the create environment. Click Create. The packages will install from the requirements file. In Powershell inside the Visual Studio run:

C:\VisualStudioPyProjects\AIFullStackApp\backend>.venv\Scripts\activate
(.venv) C:\VisualStudioPyProjects\AIFullStackApp\backend>

13) In the frontend project; right click over the packages inside the Dependencies and click restore packages. The npm modules will be installed and restored.
12) Check the the code of main.py and App.jsx
13) Right click over the solution and click the Property item over the context menu. In Configure Startup Projects menu: multiple startup projects; select start (in the dropdown) for both projects.
14) Add a file in the solution root. Right click the solution; click add new file. Add a text file. Name it: docker-compose.yml. Check the code. Run the follwig command in Git Bash (command terminal): docker compose up -d. The command will pull te wsl image for postgre sql to use for the backend.We provided a name for database in the .yml file.
