import ollama from 'ollama';


const chatBot = new ollama.Ollama();

// const chatLog = document.getElementById('chat-log');
// const user_input = document.getElementById('user-input');
// const sendButton = document.getElementById('send-button');
const response = await ollama.chat({
    model: 'granite',
    messages: [{role: 'user', content: 'Addicted WAS here'}],
    
})
client.sendMessage({
    model: 'granite', 
    prompt: 'Translate to French: Hello, how are you?',
    temperature: 0.7,
    max_tokens: 100,
  })
  .then((response) => console.log(response))
  .catch((error) => console.error('Error:', error));
console.log(response.message.content)

// let conversation = [];

// sendButton.addEventListener('click', async () => {
//     const message = user_input.value.trim();
//     if (message) {
//         try {
//             conversation.push({ role: 'user', content: message });
//             const response = await ollama.chat({
//                 model: 'llama3.1',
//                 messages: conversation,
//             });
//             conversation.push(response.message);
//             chatLog.innerHTML = '';
//             conversation.forEach((msg) => {
//                 if (msg.role === 'user') {
//                     chatLog.innerHTML += `<p>You: ${msg.content}</p>`;
//                 } else {
//                     chatLog.innerHTML += `<p>Ollama: ${msg.content}</p>`;
//                 }
//             });
//             user_input.value = '';
//         } catch (error) {
//             console.error(error);
//         }
//     }
// });
{/* <script src="https://cdn.jsdelivr.net/npm/ollama-js@latest/dist/ollama.min.js"></script> */}

