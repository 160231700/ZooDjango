function zoo_cost(){
    let adults = document.getElementById("id_zoo_adult");
    let children = document.getElementById("id_zoo_child");
    let admission_date = document.getElementById('id_valid_date').value

    if (String(admission_date) == "NaN"){
        let price = document.getElementById('zoo_output')
        price.innerHTML = "Hotel cost: Date not chosen"
    }else{
        
        let total = parseInt(adults.value) * 30
                    + parseInt(children.value) * 20
        
        let price = document.getElementById('zoo_output')
        price.innerHTML = "Hotel cost: £" + String(total)
    }
}



let adults = document.getElementById("id_zoo_adult");
adults.addEventListener("change", zoo_cost)

let children = document.getElementById("id_zoo_child");
children.addEventListener("change", zoo_cost)
