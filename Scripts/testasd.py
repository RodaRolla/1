import math
import argparse

parser = argparse.ArgumentParcer(desc='xxxx')
parcer.add_argument('radius',type= int, help='radius')
parcer.add_argument('height',type= int, help='height')
args = parser.parse_args()

def cylinder(radius,height):
	vol= (math.pi) * (radius ** 2) * (height)
	return vol

if __name__=='__main__':
	print (cylinder(args.radius, args.height))