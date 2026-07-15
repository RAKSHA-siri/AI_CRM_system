import React from "react";


function InteractionForm({data}) {


  return (
    <div>
      <h2>Interaction Details</h2>


      <p>HCP Name: {data.hcp_name}</p>
      <p>Date: {data.date}</p>
      <p>Product: {data.product}</p>
      <p>Sentiment: {data.sentiment}</p>
      <p>Materials Shared: {data.materials_shared}</p>
      <p>Notes: {data.notes}</p>


    </div>
  );
}


export default InteractionForm;

