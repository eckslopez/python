from annual import Annual
from monthly import Monthly
from datetime import datetime

def main():
    sub1 = Monthly('Bob', datetime.today())
    sub2 = Annual('Carol', datetime.today())
    sub3 = Monthly('Ted', datetime.today())
    sub4 = Annual('Alice', datetime.today())

    print(f'Subscriber: {sub1.subscriber}, Cost: {sub1.price}, Expiration: {sub1.expiration}')
    print(f'Subscriber: {sub2.subscriber}, Cost: {sub2.price}, Expiration: {sub2.expiration}')
    print(f'Subscriber: {sub3.subscriber}, Cost: {sub3.price}, Expiration: {sub3.expiration}')
    print(f'Subscriber: {sub4.subscriber}, Cost: {sub4.price}, Expiration: {sub4.expiration}')

    print('\nNormal subscriptions:\n')
    sub5 = Monthly('Fred', datetime.today())
    sub6 = Annual('Wilma', datetime.today())

    print(f'Movie: {sub5.subscriber}, Cost: {sub5.price}, Expiration: {sub5.expiration}')
    print(f'Movie: {sub6.subscriber}, Cost: {sub6.price}, Expiration: {sub6.expiration}')
    
if __name__ == "__main__":
    main()
