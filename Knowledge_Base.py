GYM_KB = {
    
    "Fatigue": "soreness and stiffness that lasts for several days",
    "Growth": "muscles that look bigger and feel thicker lately",
    "Dehydration": "dry skin and a constant lack of energy",
    "Overtrained": "a feeling of being burnt out with zero progress",
    "Anabolic": "a feeling that your body is constantly recovering and staying tight",
    "Joint Pain": "aching in your elbows, knees, or wrists after lifting",
    "Poor Pump": "muscles feeling flat and soft even during a workout",
    "Sleepy": "difficulty staying awake or focusing during the day",

   
    "Heavy Lifting": "maxing out your weights on a regular basis",
    "Eccentric Load": "slowing down the lowering part of your lifts",
    "Sweating": "soaking through your clothes every single workout",
    "No Progress": "being stuck at the same weight for a long time",
    "Sleep": "getting a solid 8 hours of rest every night",
    "High Protein": "eating plenty of meat, eggs, or protein shakes",
    "High Volume": "doing a very high number of sets and reps per session",
    "Low Carbs": "avoiding sugars and starches in your diet"
}

EXPRIENCING = [
    {
        "Id": 1,
        "Name": "Muscle Soreness",
        "Required": "Fatigue",
        "Optional": ["Heavy Lifting", "Eccentric Load"],
        "Output": "Your muscle fibers have tiny tears and inflammation that need a few days of rest to fully heal."
    },
    {
        "Id": 2,
        "Name": "Muscle Growth",
        "Required": "Growth",
        "Optional": ["Heavy Lifting"],
        "Output": "Your muscle fibers are physically expanding in size because you are challenging them with heavy weight."
    },
    {
        "Id": 3,
        "Name": "Salt Imbalance",
        "Required": "Dehydration",
        "Optional": ["Sweating"],
        "Output": "Your body is low on the basic salts it needs to send signals to your muscles, which can cause twitches."
    },
    {
        "Id": 4,
        "Name": "Systemic Stress",
        "Required": "Overtrained",
        "Optional": ["No Progress"],
        "Output": "Your stress hormones are too high, which causes your body to waste muscle instead of building it."
    },
    {
        "Id": 5,
        "Name": "Tissue Repair",
        "Required": "Anabolic",
        "Optional": ["Sleep", "High Protein"],
        "Output": "Your body is using your food and rest to patch up damaged muscle and make it stronger than before."
    },
    {
        "Id": 6,
        "Name": "Connective Tissue Wear",
        "Required": "Joint Pain",
        "Optional": ["Heavy Lifting", "High Volume"],
        "Output": "Your tendons and ligaments are taking a beating, likely because the load is exceeding their recovery rate."
    },
    {
        "Id": 7,
        "Name": "Glycogen Depletion",
        "Required": "Poor Pump",
        "Optional": ["Low Carbs", "High Volume"],
        "Output": "Your muscles lack the stored sugar (glycogen) and water needed to look full and perform explosively."
    },
    {
        "Id": 8,
        "Name": "CNS Fatigue",
        "Required": "Sleepy",
        "Optional": ["Overtrained", "Heavy Lifting"],
        "Output": "Your nervous system's ability to fire signals to your muscles is dampened, making weights feel heavier than they are."
    }
]

SOLUTIONS = [
    {
        "Id": 1, 
        "Name": "Active Recovery Protocol",
          "Required": 1,
        "Output": "Focus on active recovery (light walking) and ensure you aren't skipping the eccentric phase of your lifts." 
    },
    {
        "Id": 2, 
        "Name": "Hypertrophy Maintenance", 
        "Required": 2,
        "Output": "Continue progressive overload with heavy lifting. Ensure your caloric intake matches your growth."
    },
    {
        "Id": 3, 
        "Name": "Electrolyte Replenishment",
          "Required": 3,
        "Output": "Increase electrolyte intake (sodium, potassium, magnesium) and drink water before you feel thirsty."
    },
    {
        "Id": 4, 
        "Name": "Central Nervous System Deload",
          "Required": 4,
        "Output": "Schedule a 'deload week' immediately. Reduce your volume by 50% to lower cortisol levels."
    },
    {
        "Id": 5,
          "Name": "Anabolic Optimization",
            "Required": 5,
        "Output": "Maintain your high protein intake and 8-hour sleep schedule. This is the optimal state for hypertrophy."
    },
    {
        "Id": 6,
          "Name": "Joint Integrity Protocol", 
        "Required": 6,
        "Output": "Switch to higher rep ranges with lower weight for two weeks to allow tendons to heal without losing muscle."
    },
    {
        "Id": 7, 
        "Name": "Carbohydrate Refeed", 
        "Required": 7,
        "Output": "Increase your complex carbohydrate intake around your workout window to pull water and glucose into the muscle cells."
    },
    {
        "Id": 8, 
        "Name": "Neurological Rest",
          "Required": 8,
        "Output": "Take 2 full days off from the gym. Focus on deep sleep and avoid high-stimulant pre-workouts."
    }
]


VITAMINS = [

    {
        "Id": 1,
        "Name": "Omega-3 Fatty Acids",
        "Image": "Images/Omega-3 Fatty Acids.png",
        "Required": 1,
        "Output": "Omega-3s help reduce the inflammation caused by microscopic muscle tears."
    },

    {
        "Id": 2,
        "Name": "Creatine Monohydrate",
        "Image": "Images/Creatine Monohydrate.png",
        "Required": 2,
        "Output": "Creatine draws water into your muscle cells and increases ATP production for physical growth."
    },

    {
        "Id": 3,
        "Name": "Magnesium Glycinate",
        "Image": "Images/Magnesium Glycinate.png",
        "Required": 3,
        "Output": "Magnesium is a critical electrolyte that prevents muscle cramping and regulates electrical signals."
    },

    {
        "Id": 4,
        "Name": "Ashwagandha (KSM-66)",
        "Image": "Images/KSM-66.png",
        "Required": 4,
        "Output": "This adaptogen helps lower cortisol levels, reducing the systemic stress on your nervous system."
    },

    {
        "Id": 5,
        "Name": "Vitamin D3",
        "Image": "Images/Vitamin D3.png",
        "Required": 5,
        "Output": "This supports natural testosterone production and protein synthesis."
    },

    {
        "Id": 6,
        "Name": "Glucosamine & Chondroitin",
        "Image": "Images/Glucosamine & Chondroitin.png",
        "Required": 6,
        "Output": "These compounds provide the raw materials needed to repair joint cartilage and increase synovial fluid."
    },

    {
        "Id": 7,
        "Name": "L-Citrulline",
        "Image": "Images/L-Citrulline.png",
        "Required": 7,
        "Output": "Increases nitric oxide production, improving blood flow and nutrient delivery to 'flat' muscles."
    },

    {
        "Id": 8,
        "Name": "Vitamin B-Complex",
        "Image": "Images/Vitamin B-Complex.png",
        "Required": 8,
        "Output": "B-vitamins are essential for neurological function and converting food into the energy your CNS needs."
    }

]