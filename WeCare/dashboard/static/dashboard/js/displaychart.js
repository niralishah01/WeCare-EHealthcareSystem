const renderBarChart=(data,labels)=>{
    var ctx=document.getElementById("myChart").getContext("2d");
    var myChart=new Chart(ctx,{
        type:"bar",
        data:{
            labels:labels,
            datasets:[
                {
                    label:"Most 5 searched symtomps",
                    data:data,
                    backgroundColor: [
                        "rgba(255, 99, 132, 0.2)",
                        "rgba(54, 162, 235, 0.2)",
                        "rgba(255, 206, 86, 0.2)",
                        "rgba(75, 192, 192, 0.2)",
                        "rgba(153, 102, 255, 0.2)",
                        "rgba(255, 159, 64, 0.2)",
                      ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)",
                    ],
                    borderWidth:1, 
                },
            ],
        },
        options:{
            title:{
                display:true,
                text:"Searchcount for symptoms",
            },
        },
    });
};

function getChartData(chartData){
    // fetch("/dashboard/pivot_data")
    // .then((res)=>res.json)
    // .then((results)=>{
    //     console.log("results",results);
    //     const records=results.symptomrecord;
    //     console.log("All records",records);
    //     const [labels,data]=[
    //         Object.keys(records),
    //         Object.values(records),
    //     ];
        labels=[];
        data=[];
        for(let c in chartData){
            labels.append(c.symptom);
            data.append(c.searchcount);
        }
        renderChart(data,labels);
    //});
};