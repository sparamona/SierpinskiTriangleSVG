##
## Sierpinski triangle SVG builder
## Jonathan Sheena, February 2018
##

import svgwrite

### PARAMETERS
maxlevel=6					# how many levels of recursion
page=[1100,850]				# page size
line_stroke_width=1 		# line width
squish = 1 					# use 1 for triangles

### don't change this
levelheight = page[1]/(2**maxlevel)

# Function for line drawing	
def draw(dwg,current_group,p,w,h,level):
	dwg.add(dwg.line(start=[p[0]+w/2-w/4,p[1]+h/2],end=[p[0]+w/4+w/2,p[1]+h/2],stroke='red',stroke_width=1))
	midstroke='blue'
	outerstroke='pink'
	dwg.add(dwg.line(start=[p[0]+w/2,p[1]+h/2],
					  end  =[p[0]+w/2,p[1]+h],stroke=midstroke,stroke_width=1))
	dwg.add(dwg.line(start=[p[0]+w/2-w/4,p[1]+h/2],
					 end   =[p[0]+w/2-w/4,p[1]+h/2+levelheight],stroke=outerstroke,stroke_width=1))
	dwg.add(dwg.line(start=[p[0]+w/2+w/4,p[1]+h/2],
					 end   =[p[0]+w/2+w/4,p[1]+h/2+levelheight],stroke=outerstroke,stroke_width=1))

					 
def d(dwg,sq,level):
	if (level==maxlevel+1):
		return
	p=sq[0]
	w=sq[1][0]
	h=sq[1][1]
	#dwg.add(dwg.rect(insert=p,size=[w,h],stroke='black',stroke_width=.5,fill="none"))
	
	# First draw the main line
	draw(dwg,current_group,p,w,h,level)
	
	#1 up
	d(dwg,[[p[0]+w/4,p[1]],[w/2,h/2*squish]],level+1)
	
	#2 below
	d(dwg,[[p[0],p[1]+h/2],[w/2,h/2]],level+1)
	d(dwg,[[p[0]+w/2,p[1]+h/2],[w/2,h/2]],level+1)

	
#Main program
name="triangles"

# set up the drawing
dwg = svgwrite.Drawing(filename="triangles.svg", debug=True, size=(page[0],page[1]))

# full page border
dwg.add(dwg.rect(insert=[0,0],size=page,stroke='black',stroke_width=1,fill="none"))
current_group = dwg.add(dwg.g(id=name, stroke='red', stroke_width=3, fill='none', fill_opacity=0 ))
sq = [[0,0],page]

# start running
d(dwg,sq,1)
#dwg.add(dwg.text('Test', insert=(0, 10), fill='red'))
dwg.save()

