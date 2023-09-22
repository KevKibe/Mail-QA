const { createClient } = require('@supabase/supabase-js');
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const supabaseUrl = 'https://tmbibeachgjbddijvtcu.supabase.co'
const supabaseKey ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRtYmliZWFjaGdqYmRkaWp2dGN1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUyNzQwNTMsImV4cCI6MjAxMDg1MDA1M30.k2USg2yeAZFtC0fam46pdUbjemOtIMdEKYb8hjxKr2E'
const supabase = createClient(supabaseUrl, supabaseKey)

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.get('/auth/google/callback', async (req, res) => {
  console.log('superbase running');
  const authorizationCode = req.query.code;
});


app.post('/chat',(req,res)=>{
    res.json({"response":"Response from the server"})
})

app.post('/updatedatabase',async (req,res)=>{
    // Assuming you have obtained an access token and stored it in a variable
    const { accessToken, email } = req.body;

   // Define the table name in your Supabase project where you want to insert the token
   const tableName = 'mainusers';
 
   // Insert the access token into the specified table
   try {
    const { data, error } = await supabase
    .from(tableName)
    .upsert(
      [{ email: email, access_token: accessToken }],
      { onConflict: ['email'], returning: ['*'] } // Use 'email' for conflict resolution
    );
  
 
     if (error) {
       console.error('Error inserting access token:', error);
       return res.status(500).send('Error inserting access token');
     }
 
     console.log('Access token inserted successfully:', data);
     res.status(200).send('Access token inserted successfully');
   } catch (err) {
     console.error('Error:', err);
     res.status(500).send('Internal server error');
   }
});

app.listen(8000,(error)=>{
    console.log("listening on 8000");
});