import sys
import numpy as np
import pandas as pd

def weight_convert(input_weight,weight_unit="lb"):
    """Convert weight to lb for calculations if it is given in kg.

    Parameters
    ----------
    input_weight : float
        numeric value for weight of person
    weight_unit : {"lb","kg"}
        the unit that input_weight is given in

    Returns
    -------
    working_weight: float
        The person's weight in pounds

    Raises
    ------
    ValueError (TODO)
        if weight_unit given is not in right spot 

    Examples
    --------
    >>> person_weight = 100
    >>> weight_convert(person_weight)
    100
    >>> weight_convert(person_weight,"kg")
    220
    """
    working_weight = input_weight if weight_unit == "lb" else input_weight*2.2 if weight_unit == "kg" else ValueError
    return(round(working_weight))

def calculate_calories(inputWeight,workout_type = "non-training", delta_calories=0,weightUnit="lb"):
    """Return (approximate?) daily isocaloric needs for a given type.

    ***
    ***
    unsure yet as to whether to have `diet_type` as a separate parameter from `delta_calories` for the purpose of determining whether to switch the sign on `delta_calories`,
    or whether to just have a single `delta_calories` value including the sign
    """

    working_weight = weight_convert(inputWeight,weightUnit)
    # dictionary to hold parameters for various weights
    bmr_weight_list = [
        [100,115, {"non-training" : 1300, "light" : 1500, "moderate" : 1700, "hard" : 1900}],
        [116,130, {"non-training" : 1500, "light" : 1700, "moderate" : 1900, "hard" : 2100}],
        [131,145, {"non-training" : 1700, "light" : 1900, "moderate" : 2100, "hard" : 2300}],
        [146,160, {"non-training" : 1800, "light" : 2000, "moderate" : 2250, "hard" : 2450}],
        [161,175, {"non-training" : 1900, "light" : 2100, "moderate" : 2400, "hard" : 2600}],
        [176,190, {"non-training" : 1950, "light" : 2200, "moderate" : 2500, "hard" : 2750}],
        [191,210, {"non-training" : 2000, "light" : 2300, "moderate" : 2600, "hard" : 2900}],
        [211,230, {"non-training" : 2150, "light" : 2500, "moderate" : 2800, "hard" : 3100}],
        [231,250, {"non-training" : 2300, "light" : 2700, "moderate" : 3000, "hard" : 3300}],
        [251,275, {"non-training" : 2500, "light" : 2900, "moderate" : 3250, "hard" : 3600}],
        [276,300, {"non-training" : 2700, "light" : 3100, "moderate" : 3500, "hard" : 3900}]
    ]

    calorie_dict = {}
    for i in bmr_weight_list:
        if working_weight in range(i[0],i[1]+1):
            calorie_dict = i[2]
    calories = calorie_dict[workout_type] + delta_calories

    return(calories)

def calculate_protein(inputWeight, weightUnit="lb"):
    '''return recommended g of protein.
    weightunit is one of {lb, kg}
    inputWeight is the weight of the person
    '''

    working_weight = weight_convert(inputWeight,weightUnit)


    g_protein = working_weight
    return(g_protein)

def calculate_carbs(inputWeight,workout_type="non-training",carb_amount="recommended",weightUnit="lb"):
    """ Return minimum or recommended grams of carbs for a given training intensity.

    Parameters
    ----------
    inputWeight : int
        weight of person
    workout_type : {"non-training","light","moderate","hard"}
        intensity of workout for a given day.
    carb_amount : {"minimum","recommended"}
        whether to return the minimum or recommended number of carbs per g of bodyweight
    weightUnit : {"lb","kg"}
        Whether `inputWeight` is given in pounds or kilograms

    Returns
    -------
    g_carbs : int
        grams of carbs for the given parameters

    Examples
    --------
    >>> person_weight = 140
    >>> calculate_carbs(person_weight)
    70
    >>>calculate_carbs(person_weight,"moderate","minimum","kg")
    308
    """
    carbTable = {
        "non-training" : {"minimum" : 0.3, "recommended" : 0.5},
        "light" : {"minimum" : 0.5, "recommended" : 1.0},
        "moderate": {"minimum" : 1.0, "recommended" : 1.5},
        "hard" : {"minimum" : 1.5, "recommended" : 2.0}
    }

    working_weight = weight_convert(inputWeight,weightUnit)

    g_carbs = working_weight * carbTable[workout_type][carb_amount]

    return(round(g_carbs))

def calculate_fat(calculate_calories,g_protein,g_carbs):
    """Return grams of fat for a given day. 
    """

    g_fat = (calculate_calories - 4 * (g_carbs + g_protein))/9
    return(round(g_fat))



def generate_macronutrients_by_intensity(weight,calorie_delta):
    training_intensities = ["non-training","light","moderate","hard"]
    macronutrients_by_intensity = {}
    for training_intensity in training_intensities:
        day_cal = calculate_calories(weight,training_intensity,delta_calories=calorie_delta)
        day_pro = calculate_protein(weight)
        day_carbs = calculate_carbs(weight,training_intensity)
        day_fat = calculate_fat(day_cal,day_pro,day_carbs)
        macronutrients_by_intensity[training_intensity] = {
            "calories" : day_cal,
            "protein" : day_pro,
            "carbs" : day_carbs,
            "fat" : day_fat
        }
    return macronutrients_by_intensity
