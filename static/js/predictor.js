d3.selectAll("#fight_predict").on("click", predictFight);

function predictFight() {

    var dropdownMenu = d3.select("#weight_class option:checked").property("text");

    d3.json(`https://ufc-predict-project.herokuapp.com/data`).then(function(data) {

        console.log(data);

        // var fighter_1 = d3.select("#fighter_1 option:checked").property("text");
        // // console.log(fighter_1);
        // var fighter_2 = d3.select("#fighter_2 option:checked").property("text");
        // // console.log(fighter_2);
    
        // var fight_pair = fighter_1 + "/" + fighter_2;
        // // console.log(fight_pair);
    
        // var result = data.filter(item => {
        //     return item.fighter_pair == fight_pair;  
        // });

        d3.select('#fight_winner').selectAll('h1').data([]).exit().remove();

        console.log(result);

        if (result.winner == "Winner-Fighter 1") {

            d3.select('#fight_winner')
                .selectAll('h1')
                .data(result)
                .enter()
                .append('h1')
                .text(function(d){`Predicted Winner: ${d.fighter_2}`})
                .attr("value", function(d) {return d.fighter_1})
                .attr("id", function(d) {return d.fighter_1})
                .attr("class", "jumbotron");

        } else {

            d3.select('#fight_winner')
                .selectAll('h1')
                .data(result)
                .enter()
                .append('h1')
                .text(function(d){return `Predicted Winner: ${d.fighter_2}`})
                .attr("value", function(d) {return d.fighter_2})
                .attr("id", function(d) {return d.fighter_2})
                .attr("class", "jumbotron");

        }



    })

}