d3.selectAll("#fight_predict").on("click", predictFight);

function predictFight() {
    var fighter_1 = d3.select("#fighter_1 option:checked").property("text");
    console.log(fighter_1);
    var fighter_2 = d3.select("#fighter_2 option:checked").property("text");
    console.log(fighter_2);
    
}