from urllib.request import urlopen

print ("Launching Mercury prealpha...")

try:
	conf = open('config.conf', 'r')
	api_key = conf.read()
	print ("Config file loaded.")
	print ("API Key: " + api_key)
except IOError:
	print ("No config file. Generating config file...")
	conf = open("config.conf", 'a')
	conf = open("config.conf", 'w')
	print ("Please enter your DogeAPI API key for proper use.")
	api_key = input("API Key: ")
	conf.write(api_key)
	conf.close()
	print ("Restarting...")
	exit()

def main():
	command = input("Choose a command: ")
	if command == "help" or command == "?":
		print ("See README for valid commands. Mercury is based on DogeAPI and requires a API key to operate. If you do not have a an API key, please sign up for DogeAPI and get one.")
	elif command == "balance" or command == "bal":
		balance = urlopen("https://dogeapi.com/wow/?api_key=" + api_key + "&a=get_balance")
		for balan in balance.readlines():
			print (balan)
	elif command == "block" or command == "current_block":
		current_block = urlopen("https://dogeapi.com/wow/?a=get_current_block")
		for block in current_block.readlines():
			print (block)
	elif command == "quit" or command == "exit":
		exit()
	elif command == "addresses" or command == "my_addresses":
		my_addresses = urlopen("https://dogeapi.com/wow/?api_key=" + api_key + "&a=get_my_addresses")
		for addresses in my_addresses.readlines():
				print (addresses)
	elif command == "difficulty" or command == "get_difficulty":
		current_difficulty = urlopen("https://dogeapi.com/wow/?a=get_difficulty")
		for diff in current_difficulty.readlines():
			print (diff)	
	elif command == "new_address":
		label = input("Please choose a optional label: ")
		new_address = urlopen("https://dogeapi.com/wow/?api_key=" + api_key + "&a=get_new_address&address_label=" + label)
		for genlabel in new_address.readlines():
			print ("Address Generated.")
			print (genlabel)
	elif command == "withdraw" or command == "send":
		pmaddr = input("Please enter the payment address: ")
		samount = input("Please enter the payment amount: ")
		withdraw = urlopen("https://dogeapi.com/wow/?api_key=" + api_key + "&a=withdraw&amount=" + samount + "&payment_address=" + pmaddr)
		for sconfirm in withdraw.readlines():
			print ("Sent.")
			print (sconfirm)
	elif command == "history" or command == "address_history":
		addresshistory = input("Search by address: ")
		history = urlopen("https://dogeapi.com/wow/?api_key=" + api_key + "&a=get_address_received&payment_address=" + addresshistory)
		for hconfirm in history.readlines():
			print (hconfirm)
	elif command == "label_search" or command == "label_history"
		labelquery = input("Search by label: ")
		labelhistory = urlopen("https://dogeapi.com/wow/?api_key=" + api_key + "&a=get_address_by_label&address_label=" + labelquery)
		for lsconfirm in labelhistory.readlines():
			print (lsconfirm)
	else:
		print ("Invalid command. Please try again.")    
	main()
main()
