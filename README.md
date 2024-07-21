
<h2 align="center">RailGuard</h2>

The escalating incidences of train-wildlife collisions, especially with elephants, are a real blow
to forest-based wildlife conservation efforts. This not only endangers the animals (elephants)
but also shows significant damage to trains and railway infrastructure; hence, there is an urgent
need for effective mitigation measures and sustainable solutions for wildlife conservation. This
study recommends using Rail Guard, an innovative way of tackling this problem. To
quickly identify wild animals, such as elephants, in real-time and alert train operators, this
work relies on advanced deep learning algorithms and camera systems set at specific points
on railway tracks. Train operators can immediately slow down the trains upon receiving alerts,
ensuring that passengers and wildlife are safe. Rail Guard has the potential to enhance
wildlife conservation initiatives through data analysis, which will provide useful insights into
animal behaviour and movement patterns. Using data analytics tools provides an option to reduce
adverse impacts caused by railway expansion on various animal species, thus raising optimism
about balancing progress and preservation to reach a sustainable existence between railways and
forests.

### Number of Elephants killed on railway tracks in Kerala, India
![Rail Guard](https://github.com/gaganchapa/WildLife/blob/main/tab.png)

<h2 align="center">Real-Time Elephant Detection Web App</h2>


![](https://github.com/gaganchapa/WildLife/blob/main/main_page.png)
The Real-Time Elephant Detection web app utilizes the advanced YOLOv8 (You Only Look Once, version 8) algorithm to accurately identify elephants on railway tracks. This state-of-the-art deep learning model processes live camera feeds to detect elephants in real-time, providing instant alerts to train locopilots. Upon detection, the app triggers a buzzer notification to promptly warn the train driver of potential hazards on the tracks. This proactive alert system significantly enhances safety by allowing the train crew to take necessary precautions and prevent collisions, thereby safeguarding both wildlife and passengers. YOLOv8's high accuracy and speed make it an ideal choice for this critical application, ensuring timely and reliable elephant detection.


### Loss Plots From Trained Yolov8 model
![](https://github.com/gaganchapa/WildLife/blob/main/loss.png)

### Sample Predictions:
![](https://github.com/gaganchapa/WildLife/blob/main/pred.png)

<h2 align="center">Dash Board</h2>
![](https://github.com/gaganchapa/WildLife/blob/main/dash.png)
Dashboard provides a comprehensive suite of features for understanding elephant movements and monitoring the performance of detection systems:

* Real-Time Elephant Detection: Displays elephant sightings on a map with scatter plots, each marker representing a specific location. This visualization helps identify common pathways used by elephants, enabling route instructions to train co-pilots for enhanced safety.

* Distribution of Detected Elephants by Pole Location: Utilizes bar charts to show the number of elephants detected by each monitoring pole. This section provides insights into total detections, pole failures, and active poles, facilitating quick responses to system issues and live detections, and enabling instant survey reports.

* 3D Real-Time Elephant Detection and Monitoring: Employs 3D bar charts on a map to visualize elephant detections, with bar height indicating detection counts at specific locations. Color coding highlights threshold values, alerting personnel to areas with potentially higher elephant concentrations. This feature aids in understanding problem severity and supports surveys and analysis.

* Real-Time Monitoring of AI Model: Tracks the performance of the elephant detection model at each pole, presenting metrics such as prediction loss, CPU and memory usage, and power consumption. Integration with the Weights & Biases (wandb) monitoring system provides real-time performance metrics and report generation capabilities, ensuring the system's effectiveness and reliability.


### Installation and Setup

To run the Elephant Detection App, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/RailGuard.git
   cd RailGuard
   ```
2. **Install the required dependencies:**
   ```bash
   pip install -r req.txt
   ```
3. **Run the Streamlit app:**
   ```bash
   streamlit run main_page.py
   ```

   


