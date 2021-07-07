import hashlib
import base64
import sys




def f_md5(bytearray):

	hash = hashlib.md5()
	hash.update(bytearray)
	return hash.hexdigest()
	
def compare_first_chars(s1, s2, size):
	
	s1 = s1[0:size]
	s2 = s2[0:size]
	return s1 == s2
	
def worker(init):
	id_of_miner = f_md5("16798134".encode()) #string
	print(id_of_miner)
	CPEN_COIN = "CPEN 442 Coin" #string
	year = "2019" #string
	hash_of_proceeding_coin = "2e3a8e88a060cedcd9ac7b74fadd58e0" #string
	test_blob = init #series of bytes converted to a string.
	starting_string = "00000000" # string to compare against
	
	
	while(1):
		#create string to input to md5 hash
		bytearray = CPEN_COIN.encode() + year.encode() + hash_of_proceeding_coin.encode() + test_blob.to_bytes(length=(test_blob.bit_length()+7)//8,byteorder='big') + id_of_miner.encode()

		#hash the string, return a string
		result = f_md5(bytearray)
		
		#compare with desired result
		if(compare_first_chars(result, starting_string, len(starting_string))):
			coin_blob = test_blob.to_bytes(length=(test_blob.bit_length()+7)//8,byteorder='big')
			break
		else:
			test_blob = test_blob + 1
#			print(test_blob)
			print(result)
		

	print("the search is done!")
	print("the coin blob found is :"+coin_blob)

	bs64coin = base64.b64encode(coin_blob)
	print("the base64 encoded coin is:"+bs64coin)

worker(0)

#169,772,670
#AW3CrUE0


#
# example stuff
#
#

#miner = "d41f33d21c5b2c49053c2b1cc2a8cc84"
#blob_example_decoded = base64.b64decode('WICbUP4soPxDWXV92qR6dpP7Rhs=').decode("utf-8")

#print(blob_example_decoded)
