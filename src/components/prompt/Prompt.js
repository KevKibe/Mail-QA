import React, { useState,useEffect } from 'react';
import { Formik, Form, Field } from 'formik';
import axios from 'axios';
import TypeWriterComponent from '../../assets/js/type';

function Prompt() {
  const [response, setResponse] = useState(null);
  const [query, setQuery] = useState('');

  useEffect(() => {
    // Automatically send a request to /mainusers and print the output to the console
    axios.get('http://localhost:8000/mainusers')
      .then((response) => {
        console.log('Data from /mainusers:', response.data);
      })
      .catch((error) => {
        console.error('Error fetching data from /mainusers:', error);
      });
  }, []);

  const handleSubmit = async (values) => {
    try {
      const response = await axios.post('http://localhost:8000/chat', values);
      setResponse(response.data.response);
      setQuery(values.userInput);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <main>
      <div className="container">
        <h2 className="text-center text-primary mt-4">Mail QA</h2>

        <div className="response-container mt-4">
          <div className="query mb-4">
            <p className="txt-gradient text-center">
              {query ? query : "Please get me all emails with the keyword 'project meeting'"}
            </p>
          </div>

          <div className="response text-center">
            {query ? (
              <p className="txt-grey txt-type" data-wait="100000" data-words={JSON.stringify([response])}></p>
            ) : (
              <p className="txt-grey txt-type" data-wait="100000" data-words='["No response"]'></p>
            )}
          </div>

          {response && (
            <div className="response-container mt-4">
              <div className="response text-center">
                <p className="txt-grey txt-type" data-wait="100000" data-words={response}></p>
              </div>
              <TypeWriterComponent />
            </div>
          )}
        </div>

        <div className="form-container mt-4">
          <Formik initialValues={{ userInput: '' }} onSubmit={handleSubmit}>
            <Form>
              <div className="form-group text-center">
                <Field
                  type="text"
                  name="userInput"
                  placeholder="Enter your query"
                  className="form-control"
                  style={{ }}
                />
              </div>
              <button type="submit" className="btn btn-primary btn-block mt-3" style={{}}>
                Submit
              </button> 
            </Form>
          </Formik>
        </div>
      </div>
    </main>
  );
}

export default Prompt;
