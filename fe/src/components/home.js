import axios from "axios";
import React, { useState } from 'react';

function Home() {

    const baseURL = 'http://127.0.0.1:5000';

    const [newWord, setNewWord] = useState('');
    const [result, setResult] = useState('');

    function startSession() {
        console.log("here");
        
        axios.get(baseURL+'/startsession')
        .then((response) => {
            console.log(response);
        })
    }


    function getWordOutput () {
        axios.get(baseURL+'/getnewword')
        .then((response) => {
            console.log(response);
            setNewWord(response.data);
        })


    }

    function setResultValue (e) {
        setResult(e.target.value);
    }


    function sendResultValue () {
        const req = {
            interpreted_word : result
        }
        axios.post(baseURL+'/setresultfromgame', req)
        .then((res) => {
            console.log(res);
        })
    }

    function closeSession() {
        axios.get(baseURL+'/closesession')
        .then((response) => {
            console.log(response);
        })
    }


    return (
        <div>
            <div>
                <button onClick={startSession}>Start session</button>
            </div>
            <br></br>
            <div>
                <button onClick={getWordOutput}>Get word</button>
                <div className="getWordOutputField">{newWord}</div>
            </div>
            <br></br>
            <div>
                <input type="text" value={result} onChange={setResultValue} />
                <button onClick={sendResultValue} >Send Result</button>
            </div>
            <br></br>
            <div>
                <button onClick={closeSession}>Close session</button>
            </div>
        </div>
    )
}
export default Home;