### Setting up Amazon EC2 instance: 

##### After establishing the connection (using SSH) to our Amazon EC2 instance, I applied the following steps:

	1. update the instance software, $ sudo yum update

	2. install git on the instance, $ sudo yum install git

	3. upload the repo from Github to the instance, $ git clone https://github.com/CUBigDataClass/5Vs.git

	*File transfer commands:*

		>> If you need to transfer any file 'SampleFile.txt' from your local computer to the instance, use SCP in a new terminal window, locate your files path, then apply the following command:
		$ scp -i ~/path/5Vs.pem ~/path/SampleFile.txt ec2-user@ec2-52-10-133-241.us-west-2.compute.amazonaws.com:~

		>> If you need to transfer a file from the instance to your local computer:
		$ scp -i ~/path/5Vs.pem ec2-user@ec2-52-10-133-241.us-west-2.compute.amazonaws.com:~/path/SampleFile.txt ~/path/SampleFile2.txt

	4. install tweepy, $ sudo pip install tweepy
	
	5. install pymongo, $ sudo pip install pymongo

	6. install NLTK, $ sudo pip install -U nltk



