if __name__ == '__main__':
    N = int(input("enter number of commands:"))
    output=[]
    for i in range(N):
      A=input("enter the command(insert,print,remove,append,sort,pop,reverse):")
      l=A.split(" ")
      if l[0]=='insert':
        output.insert(int(l[1]),int(l[2]))
      elif l[0]=='print':
        print(output)  
      elif l[0]=='remove':
        output.remove(int(l[1]))
      elif l[0]=='append':
        output.append(int(l[1]))
      elif l[0]=='sort':
        output.sort()     
      elif l[0]=='pop':
        output.pop()
      elif l[0]=='reverse':
        output=output[::-1]   
      else:
          print("command does not exist! please enter valid command")
      