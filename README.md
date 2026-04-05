WHY DID I CREATE THIS ?


This is a very basic singleton design pattern with the basic purpose of rate limiting from user's end.It helps in prevention of IP ban when proxy is not rotated as it should be in a layman's fashion.This does not serves any ultimate usecase but it is a practicing module for singleton pattern.
Something creative was tried through these codes

SINGLETON DESIGN PATTERN :->

This is a design pattern specifically known for creation of only one instance.
Consider a bus platform where many buses arrive and depart.Singleton here is that bus platform and buses that arrive and depart are added attributes to it.
Consider an icecream seller.Container related to icecream can be called a singleton design pattern and icecreams in it can be called added attributes here.


WHAT'S IN THE CODE?
Have you ever seen a coincidence of getting two things by two different people at once.Such coincidence can also happen with singleton design pattern.What if two different instances are created at the same time? To ensure only single instance ,a term called "thread safety" is introduced.That is in the first block of code.

Last block of code shows attempts to rate limit the requests thrown from users end.


ENUM

Enum is said to be one of the best ways to create singleton in many programming language




