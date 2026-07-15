import React, { useState } from "react";


function ChatPanel({ updateForm }) {


  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);




  async function sendMessage(){


    const response = await fetch(
      "http://127.0.0.1:8000/chat",
      {
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body: JSON.stringify({
          message: message
        })
      }
    );




    const data = await response.json();




    updateForm(data.form_data);




    setChat([
      ...chat,
      {
        user: message,
        ai: data.response
      }
    ]);




    setMessage("");
  }




  return(
    <div>


      <h2>AI Assistant</h2>


      {chat.map((item,index)=>(
        <div key={index}>
          <p><b>User:</b> {item.user}</p>
          <p><b>AI:</b> {item.ai}</p>
        </div>
      ))}




      <input
        value={message}
        placeholder="Describe your interaction..."
        onChange={(e)=>setMessage(e.target.value)}
      />


      <button onClick={sendMessage}>
        Send
      </button>


    </div>
  );


}


export default ChatPanel;

