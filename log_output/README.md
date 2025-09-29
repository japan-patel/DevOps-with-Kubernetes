Create an application that generates a random string on startup, stores this string into memory, and outputs it every 5 seconds with a timestamp

Deploy it into your Kubernetes cluster with "kubectl create deployment log-output-dep --image=japanpatel0305/log_output_app:slim" and confirm that it's running with kubectl logs 

(Porblem 1 = no logs after running the deployment
 Solution = command to run is python -u app.py
 
 Problem 2 = no logs even after correcting the dockerfile's CMD
 solution = remove cached images from server node with crictl)
