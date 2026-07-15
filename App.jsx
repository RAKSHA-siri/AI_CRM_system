import React, { useState } from "react";
import ChatPanel from "./ChatPanel";
import InteractionForm from "./InteractionForm";


function App(){


  const [interaction, setInteraction] = useState({
    hcp_name:"",
    date:"",
    product:"",
    sentiment:"",
    materials_shared:"",
    notes:""
  });




  return(
    <div>


      <h1>AI CRM HCP Interaction</h1>


      <div style={{display:"flex", gap:"30px"}}>


        <InteractionForm data={interaction}/>


        <ChatPanel 
          updateForm={setInteraction}
        />


      </div>


    </div>
  );
}


export default App;

