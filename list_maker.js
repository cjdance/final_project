
function default_weights() {

    d3.json("http://127.0.0.1:5000/weight").then(function(test) {

    var weights = test;

    d3.select("#weight_class")
        .selectAll("option")
        .data(weights)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})


    var dropdownMenu = d3.select("#weight_class option:checked").property("value");
    
    d3.json(`http://127.0.0.1:5000/${dropdownMenu}`).then(function(data) {
    
    var fighters = data;

    fighters = fighters.sort(function (a,b) {return d3.ascending(a.name, b.name);});
    
    d3.select("#fighter_1")
            .selectAll("option")
            .data(fighters)
            .enter()
            .append("option")
            .text(function(d){return d.name})
            .attr("value", function(d) {return d.name})
            .attr("id", function(d) {return d.name})
            
    d3.select("#fighter_2")
        .selectAll("option")
        .data(fighters)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})


    var fighter = d3.select("#fighter_1 option:checked").property("text");

    var fighter_1 = data.filter(item => {
        return item.name == fighter;
    });

    d3.select('#fighter_1_title')
        .selectAll('h3')
        .data(fighter_1)
        .enter()
        .append('h3')
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})

    d3.select("#fighter_1_text")
        .selectAll('li')
        .data(fighter_1)
        .enter()
        .append('li')
        .text(function(d){return `Record (W-L-D): ${d.wins}-${d.losses}-${d.draws}`})
        .attr("value", function(d){return d.wins})
        .attr("id", `fighter_1_wins`)
        .append('li')
        .text(function(d){return `Stance: ${d.stance}`})
        .attr("value", function(d){return d.stance})
        .attr("id", `fighter_1_stance`)
        .append('li')
        .text(function(d){return `Weight: ${d.weight}`})
        .attr("value", function(d){return d.weight})
        .attr("id", `fighter_1_weight`)
        .append('li')
        .text(function(d){return `Significant Strikes Landed per Minute: ${d.SLpM}`})
        .attr("value", function(d){return d.SLpM})
        .attr("id", `fighter_1_SLpM`)
        .append('li')
        .text(function(d){return `Significant Strikes Absorbed per Minute: ${d.SApM}`})
        .attr("value", function(d){return d.SApM})
        .attr("id", `fighter_1_SApM`)
        .append('li')
        .text(function(d){return `Significant Strikes Landed Percentage: ${d.SLpct}`})
        .attr("value", function(d){return d.SLpct})
        .attr("id", `fighter_1_SLpct`)    
        .append('li')
        .text(function(d){return `Significant Strikes Defended Percentage: ${Math.round(d.SDpct*100)}%`})
        .attr("value", function(d){return d.SDpct})
        .attr("id", `fighter_1_SDpct`)           
        .append('li')
        .text(function(d){return `Take Downs Averaged per 15 Minutes: ${d.TDavg}`})
        .attr("value", function(d){return d.TDavg})
        .attr("id", `fighter_1_TDavg`)            
        .append('li')
        .text(function(d){return `Take Downs Accuracy: ${Math.round(d.TDacc*100)}%`})
        .attr("value", function(d){return d.TDacc})
        .attr("id", `fighter_1_TDacc`)        
        .append('li')
        .text(function(d){return `Submissions Attempted : ${d.subs}`})
        .attr("value", function(d){return d.subs})
        .attr("id", `fighter_1_subs`);
        
        
        var fighter = d3.select("#fighter_2 option:checked").property("text");

        var fighter_2 = data.filter(item => {
            return item.name == fighter;
        });


        console.log(fighter_2);

        var title = d3.select("#fighter_2_title");
        var list = d3.select("#fighter_2_text");

        title.selectAll('h3').data([]).exit().remove();
        list.selectAll('li').data([]).exit().remove();


        title.data(fighter_2)
            .selectAll('h3')
            .data(fighter_2)
            .enter()
            .append('h3')
            .text(function(d){return d.name})
            .attr("value", function(d) {return d.name})
            .attr("id", function(d) {return d.name});

        list.selectAll('li')
            .data(fighter_2)
            .enter()
            .append('li')
            .text(function(d){return `Record (W-L-D): ${d.wins}-${d.losses}-${d.draws}`})
            .attr("value", function(d){return d.wins})
            .attr("id", `fighter_2_wins`)
            .append('li')
            .text(function(d){return `Stance: ${d.stance}`})
            .attr("value", function(d){return d.stance})
            .attr("id", `fighter_2_stance`)
            .append('li')
            .text(function(d){return `Weight: ${d.weight}`})
            .attr("value", function(d){return d.weight})
            .attr("id", `fighter_2_weight`)
            .append('li')
            .text(function(d){return `Significant Strikes Landed per Minute: ${d.SLpM}`})
            .attr("value", function(d){return d.SLpM})
            .attr("id", `fighter_2_SLpM`)
            .append('li')
            .text(function(d){return `Significant Strikes Absorbed per Minute: ${d.SApM}`})
            .attr("value", function(d){return d.SApM})
            .attr("id", `fighter_2_SApM`)
            .append('li')
            .text(function(d){return `Significant Strikes Landed Percentage: ${d.SLpct}`})
            .attr("value", function(d){return d.SLpct})
            .attr("id", `fighter_2_SLpct`)    
            .append('li')
            .text(function(d){return `Significant Strikes Defended Percentage: ${Math.round(d.SDpct*100)}%`})
            .attr("value", function(d){return d.SDpct})
            .attr("id", `fighter_2_SDpct`)           
            .append('li')
            .text(function(d){return `Take Downs Averaged per 15 Minutes: ${d.TDavg}`})
            .attr("value", function(d){return d.TDavg})
            .attr("id", `fighter_2_TDavg`)            
            .append('li')
            .text(function(d){return `Take Downs Accuracy: ${Math.round(d.TDacc*100)}%`})
            .attr("value", function(d){return d.TDacc})
            .attr("id", `fighter_2_TDacc`)        
            .append('li')
            .text(function(d){return `Submissions Attempted : ${d.subs}`})
            .attr("value", function(d){return d.subs})
            .attr("id", `fighter_2_subs`);

    });

    })





};

default_weights();



d3.selectAll("#weight_class").on("change", updateFighters)


function updateFighters() {

    var dropdownMenu = d3.select("#weight_class option:checked").property("text");

    // console.log(dropdownMenu);
    
    d3.json(`http://127.0.0.1:5000/${dropdownMenu}`).then(function(data) {

    var fighters = data;

    d3.select("#fighter_1")
        .selectAll("option")
        .data([])
        .exit()
        .remove();

    d3.select("#fighter_1")
        .selectAll("option")
        .data(fighters)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name});
        
    d3.select("#fighter_2")
        .selectAll("option")
        .data([])
        .exit()
        .remove();

    d3.select("#fighter_2")
    .selectAll("option")
    .data(fighters)
    .enter()
    .append("option")
    .text(function(d){return d.name})
    .attr("value", function(d) {return d.name})
    .attr("id", function(d) {return d.name});

    updateCard1();
    updateCard2();

    });
}



