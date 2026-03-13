# name = ''
# password = ''
# while True:
#     print("Who are You?")
#     name = input()
#     if name != 'lol':
#         continue
#     print("It's me, pass is |-_-| (YOU KNOW!)")
#     password = input()
#     if password == '|-_-|':
#         print("flag(wowIHaveMadeItAndBreakIt)")
#         break
# print("~~~!TheFlag~~~")

no = 1
while no <= 10:  # 1. Condition makes sense (1 is <= 10)
    if no == 5:
        no += 1  # Increment before continuing to avoid infinite loop
        continue
    print(no)
    no += 1      # 2. Correct increment
