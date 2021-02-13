# Lambda to convert phone numbers to vanity phone numbers
# Save best 5 results and caller phone number in DynamoDB

# TODO:
# 1. Inputs - 10 digit phone number; check correct input
# 2. Outputs - Vanity phone numbers; save best 5 in DynamoDB
# 3. Assign numbers to letters for phone number indexed at [6-9] (2: ABC, 3: CDE, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ)
# 4. Use word/dictionary API  to convert to vanity
# 

# ASSUMPTIONS:
# - Words are between 3 to 7 letters in length
# - If phone number contains only 0,1,5,7 there are no vowels - no words
# - No dashes or parenthesis in input
# - Does not start with '1'
# - Area Code is not converted
# - No slang / misspelling

phoneNumberLettersDict = {
    '2' : ["A","B","C"] ,
    '3' : ["D","E","F"] ,
    '4' : ["G","H","I"] ,
    '5' : ["J","K","L"] ,
    '6' : ["M","N","O"] ,
    '7' : ["P","Q","R","S"] ,
    '8' : ["T","U","V"],
    '9' : ["W","X","Y","Z"]
    }

phoneNumber = input(str("What is you phone number? (please enter with area code and no dashes)"))

while phoneNumber.isdigit() == False or len(phoneNumber) != 10:
    phoneNumber = input("Only enter 10-digit phone number. Letters, spaces, and dashes are not accepted (ex 1234567890). Please re-enter phone number: ")

#remove area code - not part of vanity name
removeAreaCode = phoneNumber[3::]

#put phone number into a list 
phoneNumberList = []
phoneNumberList[:0] = removeAreaCode

#change phone number to list of list of possible letters
letterList = []
for number in phoneNumberList:
    letterList = letterList + phoneNumberLettersDict[number]
    