import asyncio
from pyscript import document
from pyodide.ffi import create_proxy
from Knowledge_Base import GYM_KB, EXPRIENCING,SOLUTIONS,VITAMINS



        
async def engine():
    user_facts = []
    
    
    Question = document.querySelector('#Question')
    Output = document.querySelector('#Output')
    yes_btn = document.querySelector('#yes-btn')
    no_btn = document.querySelector('#no-btn')
    Answer_solution = document.querySelector('#Answer_Solution')
    Vitamin_suggestion = document.querySelector('#Vitamin_suggestion') 
    vitamin_template = document.querySelector("#vitamin-row-template")
    count_span = document.querySelector('#count')

    keys = list(GYM_KB.keys())
    remaining_count = len(keys)
    count_span.innerText = remaining_count

    for key, description in GYM_KB.items():
        
        Question.innerText = f"Do you experience {description}?"

       
        click_future = asyncio.Future()

        def handle_click(event):
            
            if not click_future.done():
                click_future.set_result(event.target.id)

        
        click_proxy = create_proxy(handle_click)
        yes_btn.addEventListener("click", click_proxy)
        no_btn.addEventListener("click", click_proxy)

        
        clicked_button_id = await click_future

        
        yes_btn.removeEventListener("click", click_proxy)
        no_btn.removeEventListener("click", click_proxy)
        click_proxy.destroy() 

        
        if clicked_button_id == "yes-btn":
            user_facts.append(key)
            
        
            
        remaining_count -= 1
        count_span.innerText = remaining_count

   
    Question.innerText = "You Are Suffering From"
    
    document.querySelector('.button-group').style.display = "none"

   
    matched_results = []

    for condition in EXPRIENCING:
       
        has_required = False
        required_fact = condition["Required"]
        
        for fact in user_facts:
            if fact == required_fact:
                has_required = True
                break  

        
        has_optional = False
        optional_list = condition["Optional"]

        for opt_needed in optional_list:
            for fact in user_facts:
                if fact == opt_needed:
                    has_optional = True
                    break 
            if has_optional: 
                break 

      
        if has_required or has_optional:
            matched_results.append({
                "Id":condition["Id"],
                "Name": condition["Name"],
                "Output": condition["Output"]
            })





    user_help = []

    for solution in SOLUTIONS:
        has_exprience = False
        required_Id = solution["Required"]

        for result  in matched_results:
            if result ["Id"] == required_Id:
                has_exprience = True
                break 

        if has_exprience:
            user_help.append({
                "Name": solution["Name"],
                "Output": solution["Output"]
            })





    user_vitamins = []

    for vitamin in VITAMINS:

        has_vitamin_need = False
        required_Id = vitamin["Required"]


        for result in matched_results:
            if result["Id"] == required_Id:
                has_vitamin_need = True
                break

        if has_vitamin_need:
            user_vitamins.append({"Name": vitamin["Name"], 
                                  "Output": vitamin["Output"],
                                  "Image": vitamin["Image"]})

   
    
    Output.innerText =""
    Answer_solution.innerText = ""
    Vitamin_suggestion.innerText = ""
    

    if matched_results:
      
        for res in matched_results:
            Output.innerText += f"~{res['Name']}~\n"
            Output.innerText += f"• {res['Output']}\n\n\n"
    else:
        Output.innerText = "No Results"
        Output.innerText = "Based on your answers, we couldn't identify a specific match."

    if user_help:
        for res in user_help:
            Answer_solution.innerText += f"~{res['Name']}~\n"
            Answer_solution.innerText += f"• {res['Output']}\n\n\n\n"
    else:
        Answer_solution.innerText = "No Results"
        Answer_solution.innerText = "Based on your answers, we couldn't identify a specific Solution."




    if user_vitamins:
        for res in user_vitamins:
            vitamin_row = vitamin_template.content.firstElementChild.cloneNode(True)
            img_tag = vitamin_row.querySelector("#vitamin-image")
            name_vit = vitamin_row.querySelector("#vitamin-name")
            output_vit = vitamin_row.querySelector("#vitamin-output")

            img_tag.src = f"./{res['Image']}"
            img_tag.alt = res["Name"]
            name_vit.innerText = f"~{res['Name']}~"
            output_vit.innerText = f"• {res['Output']}"

            Vitamin_suggestion.appendChild(vitamin_row)
    else:
        Vitamin_suggestion.innerText = "No specific vitamin recommendations based on current input."

asyncio.ensure_future(engine())
