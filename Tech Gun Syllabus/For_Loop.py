#range(start, stop, step) 

#start 	Optional. An integer number specifying at which position to start. Default is 0
#stop 	Required. An integer number specifying at which position to stop (not included).
#step 	Optional. An integer number specifying the incrementation. Default is 1

for i in range(2,21,2):
    print(" ",i)


for i in range(1,11):
    print("2 *",i,"=",2*i)

Name = "sonu Sinha"
for i in range(len(Name)):
    print(Name[i],id(Name[i]))