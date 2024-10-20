***HealthWatch AI***

**Inspiration**  
The concept for HealthWatch AI emerged from witnessing my brother's struggles to receive proper medical attention while incarcerated. Medical neglect in correctional facilities is a pervasive issue, often forcing inmates to submit multiple medical requests just to be taken seriously. My vision for HealthWatch AI is to eliminate this neglect, ensuring that inmates do not have to be on the brink of a health crisis to receive the care they need.

**What It Does**  
HealthWatch AI is a healthcare management platform designed to avert the costly repercussions of delayed medical care in correctional facilities. By utilizing AI to monitor and prioritize health concerns, the system guarantees that urgent medical needs are promptly addressed, preventing the escalating costs associated with neglect.

The platform enhances transparency and accountability, motivating healthcare staff to act swiftly. Delays not only exacerbate health issues but also drive up treatment costs. HealthWatch AI helps correctional facilities save money by reducing the long-term financial burden of untreated conditions, all while ensuring inmates receive the quality care they deserve.

**Key Features**  
- **AI-Powered Prioritization of Medical Requests**: Ensures critical medical needs are addressed first, minimizing the risk of preventable deaths.  
- **Chronic Condition Tracking**: Prioritizes care based on medical requests and preexisting conditions to ensure consistent and appropriate treatment.  
- **Real-Time Metrics for Cost Reduction and Accountability**: Provides actionable data to healthcare administrators, promoting efficiency and transparency.

**Potential Impact**  
HealthWatch AI could significantly alleviate the $8 billion annual cost burden faced by correctional facilities due to inadequate healthcare. By tackling medical neglect and prioritizing urgent cases, the platform not only enhances inmate outcomes but also helps avoid escalating treatment costs stemming from delayed care.

**How We Built It**  
HealthWatch AI was developed using Next.js for the client side and Django for the backend. The core of our system leverages NLP and BERT transformers to prioritize medical requests by analyzing urgency while considering preexisting conditions. This enables effective triage, ensuring inmates receive appropriate care based on both immediate needs and their medical histories.

**Challenges We Encountered**  
One major challenge was locating accurate data. The data was difficult to obtain, often messy, and required extensive cleaning and normalization. Additionally, fine-tuning the AI model introduced another layer of complexity, as we had to balance accuracy without risking overfitting.

**What We Learned**  
We discovered that data availability was more challenging than anticipated. Much of the information we needed was behind paywalls or required official requests, which could take up to a week to process, limiting our access to relevant healthcare information.

**What's Next for HealthWatch AI**  
Our next step is to implement a real-time illness outbreak detection system. This feature would monitor health trends across correctional facilities, using AI to identify early signs of potential outbreaks or pandemics. By providing immediate alerts, HealthWatch AI could help mitigate the spread of contagious illnesses and reduce overall healthcare costs, protecting both inmates and staff.
