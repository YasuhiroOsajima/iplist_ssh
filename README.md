# SSH command line wrapper.

Get IP address to use ssh connect from Excel IP lists by searching a part of hostname.  
This tool is for Excel file style IPlist users(ex. Japanese traditional IT company).  

This tool is made to use on CentOS7 python2 environment.  

    $ pip install -r requirements.txt
    (or install PyYAML and openpyxls by OS package system like 
     yum install python-PyYAML python-openpyxl)

    $ git clone https://github.com/YasuhiroOsajima/iplist_ssh.git
    $ cd iplist_ssh/

Put your IP address Excel file lists in `listfiles` directory.  
These lists have to have structures as follow:  
- Every target host's informations (name and IP address) are in each line.  
- Each host's name is at the leftmost side column.  
- Top of host's information lines is column's name.  

Then write your IP list's setting in `conf.yaml`.  
Set each IP address column name with yaml list style.  

    manage_columns:
      - ManageLAN
      - manage ip

Install packages, and set file permission 755.  

    $ chmod 755 ssh_connector 

Exec command like this.

    $ ./ssh_connector -t hoge
    ###############################
    iplist: iplist.xlsx
    
        1:  hogehoge.jp  111.111.111.111
    ###############################
    Please select target host no. >>>  1
    Connect to hogehoge.jp : 111.111.111.111.
    ===================================================================
    user@111.111.111.111's password:
    
Connect target host and automatically get SSH terminal log in `log` directory.  

    # ls -l log/
    total 4
    -rw-r--r--. 1 user user 45 Feb 21 02:55 hogehoge.jp_20180221025502.log

If you can specify by exact hostname, exec like this.

    $ ./ssh_connector -s hogehoge.jp
