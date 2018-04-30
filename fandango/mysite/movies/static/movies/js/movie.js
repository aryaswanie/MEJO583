// Global container for movie data
window.movies = {
    params: {},
    data: {},
    genres:[]

};

function init(){
  console.log("init function");
  fetchData();
  }

$(init)




function fetchData(){
  $.getJSON('https://raw.githubusercontent.com/aryaswanie/583-final/master/fandango/mysite/data.json', function(data) {
      window.movies.data = data;
      //get genre data
      movie_genre = [];
      for (i = 0; i < window.movies.data[0]["theaters"][0]["movies"].length; i++){
        try {var temp = window.movies.data[0]["theaters"][0]["movies"][i]["genres"][0];
        movie_genre.push(temp)}
        catch (err){
          console.log("error");
        }
      }
      console.log(movie_genre);
});
}

function fillBar(){

  var svgContainer = d3.select("#movie-bar");
  var svg = d3.select("#movie-bar").append("svg").attr("height","100%").attr("width","100%");

  var chart = svg.append("g");
  svg.attr('width', '100%')
      .attr('height', 1000);
  var boundingRect = svgContainer.node().getBoundingClientRect();
  var width = boundingRect.width;
  var height = boundingRect.height;
  var x = d3.scaleLinear()
              .domain([0,18])
              .range([0,290]);

  var y = d3.scaleLinear()
              .domain([0,180])
              .range([0,width]);
  var margin = {left:50,right:50,top:40,bottom:0};
  var chartGroup = svg.append("g").attr("transform","translate("+margin.left+","+margin.top+")");

  var xAxis = d3.axisLeft(y)
  var yAxis = d3.axisBottom(x);


  svg.selectAll("rect")
        .data(window.movies.all_numbers)
        .enter().append("rect")
                  .attr("height",30 )
                  .attr("width",function(d,i){ return d*16;})
                  .attr("fill","pink")
                  .attr("y",function(d,i){ return 100+50*i; })
                  .attr("x",50 );


      chartGroup.append("g")
            .attr("class","axis y")
            .call(yAxis);

      var textArray = window.movies.all_names;
      svg.append("text").selectAll("tspan")
          .data(textArray)
          .enter().append("tspan")
            .attr("y",function(d,i){ return 115+50*i; })
            .attr("x",400)
            .attr("fill","grey")
            .attr("dominant-baseline","middle")
            .attr("text-anchor","start")
            .attr("font-size","15")
            .text(function(d){ return d; })


          var textArray2 = window.movies.all_numbers;
          svg.append("text").selectAll("tspan")
              .data(textArray2)
              .enter().append("tspan")
                .attr("height",30 )
                .attr("width",function(d,i){ return d*16;})
                .attr("y",function(d,i){ return 115+50*i; })
                .attr("x",70 )
                .attr("fill","white")
                .attr("dominant-baseline","middle")
                .attr("text-anchor","start")
                .attr("font-size","15")
                .text(function(d){ return d; });


              }
