# Get a glimpse of Perforce
## Perforce docker image
The simplest way to launch a p4 server on a PC is using the docker image:
[Perforce based on docker](https://hub.docker.com/r/ambakshi/perforce-server)

## Login the P4 server
Start the perforce docker container, then look at the "LOGS" panel of the DOCKER app, 
you can find the pre-defined user and password created by this docker image author there.

```properties
P4USER=p4admin
P4PASSWD=pass12349ers!
```
Login the p4 server with the P4 administration gui tool, P4Admin.

Create your first p4 depot.

Create a user and a user group.

We create a **standard** user here. 
```properties
P4USER=rebecca
P4PASSWD=Newuser1
```
We also create a group and add the user, rebecca, to this group. Grant the group the "admin" privilege for the depot.

Login the p4 server with the p4 gui depot management tool, P4V. Use the rebecca account
You can see the "mindwalk"depot in the "Depot" tab.

Create a workspace on your local workstation.
This step is very similar to the following git workflow:
```shell
git init
git remote add origin URL
```
Create or copy some files to the workspace, click "Add" button to mark these files "add". This step is very similar to 
this git workflow:
```shell
git add <FILES>
```
Click "Submit" button to upload these files to the p4 server. This step is very similar to this git workflow:

```shell
git commit -m "SOME COMMENT"
git push origin URL
```

Create another new workspace, "workspace2" and map it to the "mindwalk" depot, click "Get Latest" button to download/sync the latest revision
files from the remote depot to the current workspace. This step is very similar to this git workflow:
```shell
git clone URL
```
Add or edit a file in workspace2 and submit it the p4 depot. Switch to "rebecca" workspace, click "Get Latest" button o download/sync the latest revision
files from the remote depot to the current workspace. This step is very similar to this git workflow:

```shell
git pull origin URL
```

## Further reading
1. [Connecting to a unicode-mode Helix server](https://www.perforce.com/manuals/p4v/Content/P4V/using.connecting.html#Connecting_to_Helix_server)

## Reference
1. [P4admin User Guide](https://www.perforce.com/manuals/p4admin/Content/P4Admin/admin.home.html)
2. [p4 user types](https://www.perforce.com/manuals/p4sag/Content/P4SAG/managing.users.types.html)
3. [Get a glimpse of P4V](https://www.perforce.com/manuals/p4v/Content/P4V/introduction.about.html#About_P4V,_the_Helix_Visual_Client)
4. [Create a workspace](https://www.perforce.com/manuals/p4v/Content/P4V/using.workspaces.html#Creating_and_managing_workspaces)