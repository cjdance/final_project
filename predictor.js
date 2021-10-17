d3.selectAll("#fight_predict").on("click", predictFight);

function predictFight() {

    var dropdownMenu = d3.select("#weight_class option:checked").property("text");

    d3.json(`http://127.0.0.1:5000/${dropdownMenu}_predictions`).then(function(data) {

        var fighter_1 = d3.select("#fighter_1 option:checked").property("text");
        // console.log(fighter_1);
        var fighter_2 = d3.select("#fighter_2 option:checked").property("text");
        // console.log(fighter_2);
    
        var fight_pair = fighter_1 + "/" + fighter_2;
        // console.log(fight_pair);
    
        var result = data.filter(item => {
            return item.fighter_pair == fight_pair;  
        });

        // console.log(result);



    })

}