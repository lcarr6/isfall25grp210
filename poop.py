from collections import Counter
import re

# Load text from the user's message (extracted manually from the image)
text = """IS Cookies and Milk Information Session
IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester)
BYU New Student Orientation
Marriott Night,IS Academy,MSB 180 Class,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.),WAIS Events,BYU New Student Orientation
MSB 180 Class
IS Cookies and Milk Information Session
IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
Marriott Night,BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),WAIS Events
BYU New Student Orientation
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.),WAIS Events,BYU New Student Orientation
IS Cookies and Milk Information Session
IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),WAIS Events
BYU Major Fair,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),BYU New Student Orientation
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,WAIS Events
Marriott Night,BYU Major Fair,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,BYU New Student Orientation
IS Academy,MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Cookies and Milk Information Session
Marriott Night,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.),WAIS Events,BYU New Student Orientation
IS Alumni Panel (occurs during fall semester),WAIS Events
AIS Events (Opening Social, Closing Social, etc.)
WAIS Events
BYU New Student Orientation
BYU New Student Orientation
Marriott Night,BYU Major Fair,IS Cookies and Milk Information Session
Marriott Night,AIS Events (Opening Social, Closing Social, etc.),WAIS Events,BYU New Student Orientation
BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),BYU New Student Orientation
IS Cookies and Milk Information Session
IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session
BYU New Student Orientation
BYU Major Fair,MSB 180 Class,IS Cookies and Milk Information Session
BYU Major Fair,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Academy,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class
MSB 180 Class,BYU New Student Orientation
IS Cookies and Milk Information Session,BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Cookies and Milk Information Session
BYU New Student Orientation
Marriott Night,BYU Major Fair,IS Academy,IS Cookies and Milk Information Session
BYU Major Fair,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class
IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.),WAIS Events
AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
MSB 180 Class,BYU New Student Orientation
Marriott Night,IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class,BYU New Student Orientation
MSB 180 Class,IS Cookies and Milk Information Session,BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
Marriott Night,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Cookies and Milk Information Session
IS Academy,BYU New Student Orientation
Marriott Night,BYU Major Fair,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Cookies and Milk Information Session
IS Academy,MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
BYU New Student Orientation
IS Cookies and Milk Information Session
BYU Major Fair,IS Academy,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,BYU New Student Orientation
MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,MSB 180 Class,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
Marriott Night,BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class
MSB 180 Class,BYU New Student Orientation
BYU Major Fair,J Dawgs IS Information Session
Marriott Night,BYU Major Fair
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session
Marriott Night,BYU Major Fair,IS Academy,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,BYU New Student Orientation
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Cookies and Milk Information Session
Marriott Night,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session
IS Academy,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU New Student Orientation
J Dawgs IS Information Session
AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),WAIS Events
BYU New Student Orientation
BYU New Student Orientation
IS Academy,MSB 180 Class
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session
BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester)
IS Academy,IS Cookies and Milk Information Session
BYU New Student Orientation
BYU New Student Orientation
BYU Major Fair,MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU Major Fair,IS Academy,BYU New Student Orientation
J Dawgs IS Information Session,BYU New Student Orientation
MSB 180 Class
IS Academy,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
J Dawgs IS Information Session
Marriott Night,IS Academy,IS Cookies and Milk Information Session
IS Academy,IS Cookies and Milk Information Session,BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
BYU New Student Orientation
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session
IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
BYU Major Fair
IS Cookies and Milk Information Session
BYU New Student Orientation
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair
BYU Major Fair,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
BYU Major Fair,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
IS Cookies and Milk Information Session,J Dawgs IS Information Session,BYU New Student Orientation
BYU New Student Orientation
BYU New Student Orientation
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session
BYU Major Fair,IS Academy,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU Major Fair,MSB 180 Class,BYU New Student Orientation
Marriott Night,MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU Major Fair,MSB 180 Class
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU Major Fair,IS Academy,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
BYU Major Fair
BYU New Student Orientation
BYU Major Fair,MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
MSB 180 Class,IS Cookies and Milk Information Session,BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,BYU New Student Orientation
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,AIS Events (Opening Social, Closing Social, etc.)
IS Cookies and Milk Information Session
IS Academy,IS Cookies and Milk Information Session,BYU New Student Orientation
MSB 180 Class,IS Cookies and Milk Information Session
AIS Events (Opening Social, Closing Social, etc.)
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,BYU New Student Orientation
BYU New Student Orientation
BYU New Student Orientation
IS Cookies and Milk Information Session
Marriott Night,BYU Major Fair,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.),WAIS Events
AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair
BYU Major Fair,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session
BYU New Student Orientation
BYU Major Fair,IS Academy,J Dawgs IS Information Session
IS Academy
IS Cookies and Milk Information Session
BYU Major Fair,MSB 180 Class
BYU New Student Orientation
MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Cookies and Milk Information Session
AIS Events (Opening Social, Closing Social, etc.)
IS Cookies and Milk Information Session
BYU New Student Orientation
MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
Marriott Night,IS Academy,BYU New Student Orientation
BYU New Student Orientation
Marriott Night,IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class
IS Academy,MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session,IS Alumni Panel (occurs during fall semester),AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
IS Academy,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,MSB 180 Class,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,MSB 180 Class
IS Cookies and Milk Information Session,BYU New Student Orientation
BYU Major Fair,IS Academy
BYU New Student Orientation
MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class
BYU Major Fair,IS Cookies and Milk Information Session
AIS Events (Opening Social, Closing Social, etc.)
MSB 180 Class
AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU New Student Orientation
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
BYU Major Fair
MSB 180 Class
IS Academy,IS Cookies and Milk Information Session
IS Cookies and Milk Information Session
BYU Major Fair,IS Academy,IS Cookies and Milk Information Session
Marriott Night
BYU New Student Orientation
AIS Events (Opening Social, Closing Social, etc.)
IS Alumni Panel (occurs during fall semester)
IS Academy
BYU Major Fair
Marriott Night,BYU Major Fair,BYU New Student Orientation
MSB 180 Class,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,AIS Events (Opening Social, Closing Social, etc.),BYU New Student Orientation
AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU New Student Orientation
AIS Events (Opening Social, Closing Social, etc.)
IS Academy,IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
Marriott Night,BYU Major Fair,BYU New Student Orientation
MSB 180 Class,IS Cookies and Milk Information Session,J Dawgs IS Information Session,BYU New Student Orientation
Marriott Night,BYU Major Fair,IS Cookies and Milk Information Session,J Dawgs IS Information Session,BYU New Student Orientation
BYU New Student Orientation
IS Cookies and Milk Information Session,AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair
BYU New Student Orientation
IS Cookies and Milk Information Session
BYU New Student Orientation
AIS Events (Opening Social, Closing Social, etc.)
BYU Major Fair,MSB 180 Class,IS Cookies and Milk Information Session
BYU Major Fair,IS Cookies and Milk Information Session
IS Cookies and Milk Information Session,J Dawgs IS Information Session,AIS Events (Opening Social, Closing Social, etc.),WAIS Events"""

# Split lines
lines = [line.strip() for line in text.split("\n") if line.strip()]

# Count occurrences of unique statements
counter = Counter(lines)

# Get top 20 most common
most_common = counter.most_common(20)
most_common

