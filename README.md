<h1>Banana Ripeness Detection</h1>

<p>A Streamlit web app that uses a TensorFlow model to check if a banana is Ripe or Unripe.</p>

<p><em>GET 324 Mini Project, Group EE20</em></p>

<hr>

<h2>What It Does</h2>
<p>
Upload a photo of a banana. The app first checks that the photo actually contains a banana, then
predicts whether it is Ripe or Unripe, along with a confidence percentage.
</p>

<h3>How It Works</h3>
<ul>
  <li>A pre-trained MobileNetV2 model (trained on ImageNet) checks the image for banana-related labels before anything else runs</li>
  <li>If no banana-related label is found, the app rejects the image and asks for a clearer photo</li>
  <li>If the image passes, it is resized to 224 x 224 and normalized before being sent to the custom ripeness model</li>
  <li>The custom model (<code>banana_model.keras</code>) outputs a probability, with values above 0.5 read as Unripe and values at or below 0.5 read as Ripe</li>
  <li>Predictions with confidence between 0.4 and 0.6 are flagged as uncertain instead of forcing an answer</li>
</ul>

<h3>Built With</h3>
<ul>
  <li>Python</li>
  <li>TensorFlow / Keras</li>
  <li>Streamlit</li>
  <li>MobileNetV2 (ImageNet)</li>
  <li>NumPy and Pillow</li>
</ul>

<hr>

<h2>How To Set It Up</h2>

<h3>1. Clone the repo</h3>
<pre>
git clone https://github.com/petersemmanuel13092006-code/EE20-Project.git
cd EE20-Project
</pre>

<h3>2. Install dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Make sure the model file is present</h3>
<p>
<code>banana_model.keras</code> needs to sit in the same folder as <code>app.py</code>. Without it,
the app cannot run a ripeness prediction.
</p>

<h3>4. Run the app</h3>
<pre>
streamlit run app.py
</pre>
<p>
Open the local link shown in your terminal (usually <code>http://localhost:8501</code>), upload a
banana photo, and view the result.
</p>

<hr>

<h2>Known Limitations</h2>
<ul>
  <li>Only classifies two stages, Ripe or Unripe, not finer stages like green, turning, or overripe</li>
  <li>The banana validation step only checks for a general banana or fruit label, so it may still let through unusual or unclear photos</li>
  <li>Prediction accuracy depends on image clarity and lighting</li>
</ul>

<hr>

<h2>Contributors</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Reg Number</th>
      <th>Github Username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Akpadiaha, Favour Sampson</td>
      <td>23/EG/EE/009</td>
      <td>favian667</td>
    </tr>
    <tr>
      <td>Udontah, Victor Ekerette</td>
      <td>23/EG/EE/019</td>
      <td>dannyjnr12</td>
    </tr>
     <tr>
      <td>Samuel, Wisdom Uforo</td>
      <td>23/EG/EE/029</td>
      <td>wisdom77434</td>
    </tr>
    <tr>
      <td>Jack, Goodgift Emmanuel</td>
      <td>23/EG/EE/069</td>
      <td>Etilord001</td>
    </tr>
    <tr>
      <td>Peters, Emmanuel Sylvanus</td>
      <td>23/EG/EE/079</td>
      <td>petersemmanuel13092006-code</td>
    </tr>
    <tr>
      <td>Edward, Cletus Nse</td>
      <td>23/EG/EE/089</td>
      <td>Edwardcletus-bot</td>
    </tr>
    <tr>
      <td>Adu, Peter Oluwalayomi</td>
      <td>24/EG/EE/369</td>
      <td>kilo2026</td>
    </tr>
   
  </tbody>
</table>

<hr>

<h2>License</h2>
<p>For academic use only, as part of the GET 324 course.</p>
