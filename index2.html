<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>WhatThisApp</title>
    <style>

      body {
        font: 1.1em sans-serif;
        margin:0;
        padding:0;
        
      }

      html{
        width: 100%;
        height: 100vh;
        margin:0;
        padding:0;
        color:rgb(41,41,41);
      }
      header{
        width:100%;
        height:8vh;

        background-color:rgb(1,230,117);/* color:rgb(30,190,165) cyan */


      }
      header h1{
        width:100%;
        padding-top:15px;
        text-align: center;
        font-size:1.5em;
        margin:0;
        
      }

      .section_1{
        width: 100%;
        height: 42vh;
        margin-top:30px;
      }
      .section_2{
        width: 100%;
        height: 50vh;
        position: relative;
        left: 25%;
      }

      #chart{
        width: 800px;

        margin: 0 auto;
        margin-top:50px;
      }
      .background {
        fill: #eee;
      }

      line {
        stroke: #fff;
      }

      text.active {
        fill: red;
      }

      .day {
        fill: #fff;
        stroke: #ccc;
      }

      .month {
        fill: none;
        stroke: #fff;
        stroke-width: 4px;
      }
      .year-title {
        font-size: 1.5em;
      }

      /* color ranges */
        
      .RdYlGn .q0-11{fill:rgb(255,255,191)}
      .RdYlGn .q1-11{fill:rgb(217,239,139)}
      .RdYlGn .q2-11{fill:rgb(166,217,106)}
      .RdYlGn .q3-11{fill:rgb(102,189,99)}
      .RdYlGn .q4-11{fill:rgb(26,152,80)}
      .RdYlGn .q5-11{fill:rgb(0,104,55)}

      /* hover info */
      #tooltip {
        background-color: #fff;
        border: 2px solid #ccc;
        padding: 10px;
      }
     
      

      path {  stroke: #fff; }
      path:hover {  opacity:0.9; }
      rect:hover {  fill:blue; }
      .axis {  font: 10px sans-serif; }
      .legend tr{    border-bottom:1px solid grey; }
      .legend tr:first-child{    border-top:1px solid grey; }

      .axis path, .axis line {
        fill: none;
        stroke: #000;
        shape-rendering: crispEdges;
      }

      .x.axis path {
        display: none;
      }
      .legend{
          margin-bottom:76px;
          display:inline-block;
          border-collapse: collapse;
          border-spacing: 0px;
      }
      .legend td{
          padding:4px 5px;
          vertical-align:bottom;
      }
      .legendFreq, .legendPerc{
          align:right;
          width:50px;
      }
    </style>
  </head>
  <body>
      <header> <h1> WhatThisApp </h1> </header>
      <div id="chart" class="clearfix section_1"></div>
      <div id='dashboard' class='section_2'>
      </div>
  </body>
</html>

    <body>

    <div id="chart" class="clearfix"></div>

    <script src="http://d3js.org/d3.v3.js"></script>
    <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
    <script>
      var width = 960,
          height = 350,
          cellSize = 15; 

      var no_months_in_a_row = Math.floor(width / (cellSize * 7+ 50));
      var shift_up = cellSize * 3;

      var day = d3.time.format("%w"), 
          day_of_month = d3.time.format("%e") 
          day_of_year = d3.time.format("%j")
          week = d3.time.format("%U"), 
          month = d3.time.format("%m"), 
          year = d3.time.format("%Y"),
          format = d3.time.format("%Y-%m-%d");

      var color = d3.scale.quantize()
          .domain([0, 100])
          .range(d3.range(6).map(function(d) { return "q" + d + "-11"; }));

      var svg = d3.select("#chart").selectAll("svg")
          .data(d3.range(2017, 2018))
        .enter().append("svg")
          .attr("width", width)
          .attr("height", height)
          .attr("class", "RdYlGn")
        .append("g")

      var rect = svg.selectAll(".day")
          .data(function(d) { 
            return d3.time.days(new Date(d, 0, 1), new Date(d + 1, 0, 1));
          })
        .enter().append("rect")
          .attr("class", "day")
          .attr("width", cellSize)
          .attr("height", cellSize)
          .attr("x", function(d) {
            var month_padding = 1.2 * cellSize*7 * ((month(d)-1) % (no_months_in_a_row));
            return day(d) * cellSize + month_padding; 
          })
          .attr("y", function(d) { 
            var week_diff = week(d) - week(new Date(year(d), month(d)-1, 1) );
            var row_level = Math.ceil(month(d) / (no_months_in_a_row));
            return (week_diff*cellSize) + row_level*cellSize*8 - cellSize/2 - shift_up;
          })
          .datum(format);

      var month_titles = svg.selectAll(".month-title")  
            .data(function(d) { 
              return d3.time.months(new Date(d, 0, 1), new Date(d + 1, 0, 1)); })
          .enter().append("text")
            .text(monthTitle)
            .attr("x", function(d, i) {
              var month_padding = 1.2 * cellSize*7* ((month(d)-1) % (no_months_in_a_row));
              return month_padding;
            })
            .attr("y", function(d, i) {
              var week_diff = week(d) - week(new Date(year(d), month(d)-1, 1) );
              var row_level = Math.ceil(month(d) / (no_months_in_a_row));
              return (week_diff*cellSize) + row_level*cellSize*8 - cellSize - shift_up;
            })
            .attr("class", "month-title")
            .attr("d", monthTitle);

      var year_titles = svg.selectAll(".year-title") 
            .data(function(d) { 
              return d3.time.years(new Date(d, 0, 1), new Date(d + 1, 0, 1)); })
          .enter().append("text")
            .text(yearTitle)
            .attr("x", function(d, i) { return width/2 - 100; })
            .attr("y", function(d, i) { return cellSize*4.5 - shift_up; })
            .attr("class", "year-title")
            .attr("d", yearTitle);



      var tooltip = d3.select("#dashboard")
        .append("div").attr("id", "tooltip")
        .style("position", "absolute")
        .style("z-index", "10")
        .style("visibility", "hidden")
        .text("a simple tooltip");

      d3.csv("Données2.csv", function(error, csv) {
        var data = d3.nest()
          .key(function(d) { return d.Date; })
          .rollup(function(d) { return d[0].NbMessage; })
          .map(csv);

        rect.filter(function(d) { return d in data; })
            .attr("class", function(d) { return "day " + color(data[d]); })
          .select("title")
            .text(function(d) { return d + ": " + (data[d]); });

        //  Tooltip
        rect.on("mouseover", mouseover);
        rect.on("mouseout", mouseout);
        function mouseover(d) {
          tooltip.style("visibility", "visible");
          var nb_message = (data[d] !== undefined) ? (data[d]) :(0);
          var purchase_text = d + ": " + nb_message;

          tooltip.transition()        
                      .duration(200)      
                      .style("opacity", .9);      
          tooltip.html(purchase_text)  
                      .style("left", (d3.event.pageX)+30 + "px")     
                      .style("top", (d3.event.pageY) ); 
        }
        function mouseout (d) {
          tooltip.transition()        
                  .duration(500)      
                  .style("opacity", 0); 
          var $tooltip = $("#tooltip");
          $tooltip.empty();
        }

      });

      function dayTitle (t0) {
        return t0.toString().split(" ")[2];
      }
      function monthTitle (t0) {
        return t0.toLocaleString("Fr", { month: "long" });
      }
      function yearTitle (t0) {
        return t0.toString().split(" ")[3];
      }
    </script>

    <div id='dashboard'></div>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script>
    function dashboard(id, fData){
        var barColor = 'steelblue';

        function segColor(c){ return {Quentin:"#807dba", Simon:"#e08214",Hadrien:"#41ab5d", Ulysse:"#F7D358"}[c]; }
        
        // total par participant
        fData.forEach(function(d){d.total=d.freq.Quentin+d.freq.Simon+d.freq.Hadrien+d.freq.Ulysse;});
        
        // histogramme
        function histoGram(fD){
            var hG={},    hGDim = {t: 60, r: 0, b: 30, l: 0};
            hGDim.w = 500 - hGDim.l - hGDim.r, 
            hGDim.h = 300 - hGDim.t - hGDim.b;
                
           
            var hGsvg = d3.select(id).append("svg")
                .attr("width", hGDim.w + hGDim.l + hGDim.r)
                .attr("height", hGDim.h + hGDim.t + hGDim.b).append("g")
                .attr("transform", "translate(" + hGDim.l + "," + hGDim.t + ")");

            // x-axis map
            var x = d3.scale.ordinal().rangeRoundBands([0, hGDim.w], 0.1)
                    .domain(fD.map(function(d) { return d[0]; }));

            hGsvg.append("g").attr("class", "x axis")
                .attr("transform", "translate(0," + hGDim.h + ")")
                .call(d3.svg.axis().scale(x).orient("bottom"));

            // y-axis map
            var y = d3.scale.linear().range([hGDim.h, 0])
                    .domain([0, d3.max(fD, function(d) { return d[1]; })]);

            // barres
            var bars = hGsvg.selectAll(".bar").data(fD).enter()
                    .append("g").attr("class", "bar");
            
            //rectangles
            bars.append("rect")
                .attr("x", function(d) { return x(d[0]); })
                .attr("y", function(d) { return y(d[1]); })
                .attr("width", x.rangeBand())
                .attr("height", function(d) { return hGDim.h - y(d[1]); })
                .attr('fill',barColor)
                .on("mouseover",mouseover)
                .on("mouseout",mouseout);
                
            //label des barres
            bars.append("text").text(function(d){ return d3.format(",")(d[1])})
                .attr("x", function(d) { return x(d[0])+x.rangeBand()/2; })
                .attr("y", function(d) { return y(d[1])-5; })
                .attr("text-anchor", "middle");
            
            function mouseover(d){  
                var st = fData.filter(function(s){ return s.State == d[0];})[0],
                    nD = d3.keys(st.freq).map(function(s){ return {type:s, freq:st.freq[s]};});
                   
                // update    
                pC.update(nD);
                leg.update(nD);
            }
            
            function mouseout(d){      
                pC.update(tF);
                leg.update(tF);
            }
            
            hG.update = function(nD, color){
                //  y-axis map
                y.domain([0, d3.max(nD, function(d) { return d[1]; })]);
                
                var bars = hGsvg.selectAll(".bar").data(nD);
                
                // transition 
                bars.select("rect").transition().duration(500)
                    .attr("y", function(d) {return y(d[1]); })
                    .attr("height", function(d) { return hGDim.h - y(d[1]); })
                    .attr("fill", color);

                bars.select("text").transition().duration(500)
                    .text(function(d){ return d3.format(",")(d[1])})
                    .attr("y", function(d) {return y(d[1])-5; });            
            }        
            return hG;
        }
        function pieChart(pD){
            var pC ={},    pieDim ={w:250, h: 250};
            pieDim.r = Math.min(pieDim.w, pieDim.h) / 2;
                    
            // svg
            var piesvg = d3.select(id).append("svg")
                .attr("width", pieDim.w).attr("height", pieDim.h).append("g")
                .attr("transform", "translate("+pieDim.w/2+","+pieDim.h/2+")");
            
            // camembert
            var arc = d3.svg.arc().outerRadius(pieDim.r - 10).innerRadius(0);

            var pie = d3.layout.pie().sort(null).value(function(d) { return d.freq; });

            piesvg.selectAll("path").data(pie(pD)).enter().append("path").attr("d", arc)
                .each(function(d) { this._current = d; })
                .style("fill", function(d) { return segColor(d.data.type); })
                .on("mouseover",mouseover).on("mouseout",mouseout);

            // update
            pC.update = function(nD){
                piesvg.selectAll("path").data(pie(nD)).transition().duration(500)
                    .attrTween("d", arcTween);
            }      
            function mouseover(d){
              
                hG.update(fData.map(function(v){ 
                    return [v.State,v.freq[d.data.type]];}),segColor(d.data.type));
            }
            
            function mouseout(d){

                hG.update(fData.map(function(v){
                    return [v.State,v.total];}), barColor);
            }
            function arcTween(a) {
                var i = d3.interpolate(this._current, a);
                this._current = i(0);
                return function(t) { return arc(i(t));    };
            }    
            return pC;
        }
        
        // legende
        function legend(lD){
            var leg = {};
                
            
            var legend = d3.select(id).append("table").attr('class','legend');
            
            
            var tr = legend.append("tbody").selectAll("tr").data(lD).enter().append("tr");
                
            
            tr.append("td").append("svg").attr("width", '16').attr("height", '16').append("rect")
                .attr("width", '16').attr("height", '16')
          .attr("fill",function(d){ return segColor(d.type); });
                
            tr.append("td").text(function(d){ return d.type;});

            tr.append("td").attr("class",'legendFreq')
                .text(function(d){ return d3.format(",")(d.freq);});

            tr.append("td").attr("class",'legendPerc')
                .text(function(d){ return getLegend(d,lD);});

            leg.update = function(nD){
   
                var l = legend.select("tbody").selectAll("tr").data(nD);

                l.select(".legendFreq").text(function(d){ return d3.format(",")(d.freq);});

                l.select(".legendPerc").text(function(d){ return getLegend(d,nD);});        
            }
            
            function getLegend(d,aD){ 
                return d3.format("%")(d.freq/d3.sum(aD.map(function(v){ return v.freq; })));
            }

            return leg;
        }
        
        // totaux
        var tF = ['Quentin','Simon','Hadrien','Ulysse'].map(function(d){ 
            return {type:d, freq: d3.sum(fData.map(function(t){ return t.freq[d];}))}; 
        });    
        
        var sF = fData.map(function(d){return [d.State,d.total];});

        var hG = histoGram(sF), 
            pC = pieChart(tF), 
            leg= legend(tF); 
    }
    </script>

    <script>
    var freqData=[
    {State:'Janvier',freq:{Quentin:250, Simon:215, Hadrien:30, Ulysse:56}}
    ,{State:'Fevrier',freq:{Quentin:253, Simon:205, Hadrien:66, Ulysse:231}}
    ,{State:'Mars',freq:{Quentin:143, Simon:201, Hadrien:41, Ulysse:44}}
    ,{State:'Avril',freq:{Quentin:242, Simon:220, Hadrien:41, Ulysse:78}}
    ,{State:'Mai',freq:{Quentin:214, Simon:324, Hadrien:95, Ulysse:180}}
    ,{State:'Juin',freq:{Quentin:97, Simon:174, Hadrien:36, Ulysse:103}}
    ,{State:'Juillet',freq:{Quentin:224, Simon:262, Hadrien:119, Ulysse:152}}
    ,{State:'Aout',freq:{Quentin:285, Simon:433, Hadrien:128, Ulysse:149}}
    ,{State:'Sept',freq:{Quentin:204, Simon:260, Hadrien:82, Ulysse:185}}
    ,{State:'Oct',freq:{Quentin:148, Simon:155, Hadrien:86, Ulysse:76}}
    ,{State:'Nov',freq:{Quentin:154, Simon:143, Hadrien:73, Ulysse:87}}
    ,{State:'Dec',freq:{Quentin:142, Simon:192, Hadrien:135, Ulysse:80}}
    ];

    dashboard('#dashboard',freqData);
    </script>
  </body>
</html>

