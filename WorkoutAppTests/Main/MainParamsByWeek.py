#Each of these is one of the week types of 

# Format for waves is [intensity],[sets],[reps],[rest],[RIR]


# currently, I have bootstrapped this by adding Weekx_ in front of the thing's name to order them. I want to include a key called "order", but it hasnt worked yet

Week1_Accumulation = {
	"Eights" : [[0.65],[8],[5,'max'],[1.25,4],['2-3']],
	"Fives" : [[0.7],[6],[5,'max'],[3,7],['2-3']],
	"Threes" : [[0.75],[7],[3],[3],['2-3']],
	}

Week2_Intensification = {
	"Eights" : [[0.725],[8],[3,'max'],[2,4],['1-2']],
	"Fives" : [[0.65,0.725,0.775],[6],[2,2,5],[3,7],['1-2']],
	"Threes" : [[0.75],[7],[3],[3],['1-2']],
	}
	
Week3_Realization = {
	"Eights" : [[0.5,0.6,0.7,0.75,0.8],[5],[5,3,2,1,'max'],[2],['0']],
	"Fives" : [[0.5,0.6,0.7,0.75,0.8,0.85],[6],[5,3,2,1,1,'max'],[2.5],['0']],
	"Threes" : [[0.5,0.6,0.7,0.75,0.8,0.85,0.9],[7],[5,3,2,1,1,1,'max'],[2.5],['0']],
	}

Week4_Deload = {
	"Eights" : [[0.4,0.5,0.6],[3],[5],[2],['4-5']],
	"Fives" : [[0.4,0.5,0.6],[3],[5],[2],['4-5']],
	"Threes" : [[0.4,0.5,0.6],[3],[5],[2],['4-5']],
	}

#Specials is for particular exercises that vary with not only the wave, but the week in a multi-element pattern
_Specials = {
							#Intensity, sets, reps, rest, RIR
		"Alactic Power" : { "Accumulation" : [['max'],[10],[2],[1.5],['N/A']], 
							"Intensification" : [['more than last time'],[8],[2],[1.5],['N/A']],
							"Realization" :  [['more than last time'],[6],[2],[1.5],['N/A']]
							},
		


		"Alactic Capacity" : { "Accumulation" : [['max'],[2],['4 sets of 3 reps with 30sec between reps'],[2.5],['N/A']],
							   "Intensification" : [['same as last time'],[2],['5 sets of 3 reps with 30sec between reps'],[2.5],['N/A']],
							   "Realization" : [['same as last time'],[2],['6 sets of 3 reps with 30sec between reps'],[2.5],['N/A']]
							   },

		"Sprints" : { "Accumulation" : [['max'],[2],['10 x 10 meters with 1 min between sprints'],[5],['N/A']],
		              "Intensification" : [['max'],[2],['7 x 15 meters with 1.5 min between sprints'],[5],['N/A']],
		              "Realization" : [['max'],[2],['6 x 20 meters with 2 min between sprints'],[5],['N/A']]
		              }
					
		} 


_DeadPress = {

	"Eights" : { "Accumulation" :[[0.6],[8],[1],[0.5],['N/A']],
				"Intensification" :[[0.6],[10],[1],[0.5],['N/A']],
				"Realization" : [[0.6],[12],[1],[0.5],['N/A']]
				},

	"Fives" : { "Accumulation" :[[0.65],[9],[1],[0.75],['N/A']],
				"Intensification" :[[0.7],[7],[1],[1],['N/A']],
				"Realization" : [[0.75],[5],[1],[1.25],['N/A']]
				},

	"Threes" : { "Accumulation" :[[0.8,0.825,0.85],[3],[1],[1.5],['N/A']],
				"Intensification" :[[0.825,0.85,0.875],[3],[1],[2],['N/A']],
				"Realization" : [[0.875,0.95,1],[3],[1],[2.5],['N/A']]
				}

				}