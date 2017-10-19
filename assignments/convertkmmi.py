def print_menu():
 print('1. Kilometres to Miles')
 print('2. Miles to Kilometres')

def km_miles():
 print('Distance in miles: {}'.format(float(input('Enter distance in kilometres: '))/1.609))

def miles_km():
 print('Distance in kilometres: {}'.format(float(input('Enter distance in miles: '))*1.609))

if __name__ == '__main__':
 print_menu()
 choice = input('Which conversion would you like to do?:')
 if choice == '1':
  km_miles()
 elif choice == '2':
  miles_km()
