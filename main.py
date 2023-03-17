from eth_account import Account

Account.enable_unaudited_hdwallet_features()

mnemonics_filename = input("Input name of file with mnemonics: ")
results_filename = input("Input name of file with addresses (output): ")

mnemonics = open(mnemonics_filename, 'r')
results = open(results_filename, 'w+')

counter = 1

for mnemonic in mnemonics:
    try:
        acct = Account.from_mnemonic(mnemonic.rstrip())
        results.write(acct.address+"\n")
        print(str(counter) + " | " + mnemonic + " -> " + str(acct.address)+"\n")
    except:
        print(str(counter) + " | ""Something is wrong! Check your mnemonic on the line " + str(counter)+"\n")
        continue
    counter += 1

print("Check " + results_filename + ".txt")