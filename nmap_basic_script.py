def nmap(ip):
    var = f"nmap -sVC -p- -Pn -T4 --open -O {ip} -vv "
    print(var)

nmap(input("What Ip would you like to analyze today? "))
