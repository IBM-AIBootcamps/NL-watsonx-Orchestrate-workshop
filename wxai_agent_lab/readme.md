# Hands-on Lab: watsonx.ai Agent Lab

## Introduction

In this hands-on lab, you will learn how to build agentic workflows using AgentLab, a powerful tool for creating custom AI-powered agents. You will follow the story of Billie, a banker who wants to use AI to help with her workload.

Through a series of exercises, you will learn how to:

* Create a custom agent using watsonx.ai AgentLab
* Use Large Language Models (LLMs) in your agent
* Use tools to access information not previously trained into the LLM
* Trace the agent's ReAct process
* Incorporate business logic into your agent using custom tools

## Contents

- [Hands-on Lab: watsonx.ai Agent Lab](#hands-on-lab-watsonxai-agent-lab)
  - [Introduction](#introduction)
  - [Contents](#contents)
  - [Prerequisites](#prerequisites)
  - [Lab Objectives](#lab-objectives)
  - [Lab Instructions](#lab-instructions)
    - [Step 1: Get started with Agent Lab](#step-1-get-started-with-agent-lab)
    - [Step 2: Add a `Google search` tool](#step-2-add-a-google-search-tool)
    - [Step 3: Add a `Webcrawler` tool](#step-3-add-a-webcrawler-tool)
    - [Step 4: Ingest documents for Q\&A](#step-4-ingest-documents-for-qa)
    - [Step 5: Deploy your Agent](#step-5-deploy-your-agent)
    - [Step 6: (Optional) New agent with a Custom Tool](#step-6-add-a-custom-tool)
  - [Conclusion](#conclusion)
  - [Additional Resources](#additional-resources)

## Environment access
 
 - First make sure you are logged out of IBM Cloud. -> https://cloud.ibm.com/logout
 - IBM Cloud Login
    - Url: https://cloud.ibm.com/authorize/itzwatsonx3
    - Username: user_687bfa44d3@techzone.ibm.com
    - Password: Password will be provided.
 - In the left menu bar click on **Resource list**, then in the **AI / Machine Learning** section find and click on **watsonx.ai Studio**.
 - Next to the Launch in button click on dropdown arrow buton and select **IBM watsonx**.
 - On the IBM watsonx.ai welcome screen, scroll down and click the plus button in the projects section to create a project.
 - Name your project with a unique name (For example, include your name.)
 - Finish by clicking the Create button.
<!-- You must have access to a watsonx.ai SaaS environment and an initialized project within that environment. If you do not have one already, it can be provisioned on [TechZone](https://techzone.ibm.com/collection/tech-zone-certified-base-images/journey-watsonx) by selecting the **watsonx.ai/.governance SaaS** environment and selecting **Education** as **Purpose**. -->


## Lab Objectives

* Create a custom tool to access information not previously trained into an LLM
* Use the WebCrawler tool to extract information from a specific web page
* Use RAG to incorporate new information into an existing agent
* Deploy an agent with a custom tool to incorporate business logic

## Lab Instructions

### Step 1: Get started with Agent Lab

1. From the [watsonx.ai home page](https://dataplatform.cloud.ibm.com/wx/home?context=wx), navigate to a project, and then click the **New asset > Build an AI agent to automate tasks** tile.

    ![image](./images/agentlab-1.png)

2. Associate service if watsonx.ai Runtime service is not detected by clicking on **Associate Service** and click on the **Checkbox** next to available instance of watsonx.ai Runtime. Then click on **Associate** button. Then back to creating Your **New asset** from point 1.
    
3. Select a foundation model and optionally update model parameters. Let's use model `llama-3-2-90b-vision-instruct`. For details, see [Foundation model configuration](#model).
    
4. To set up your agent, specify a name for the agent and describe the tasks the agent performs in the **Setup** section.
    - Set the name to something like `<YOUR-PREFIX>-watsonx-banking-agent`. Please use e.g. your last name or another unique string within this Lab as a prefix, so that you can distinguish your agent from the agents of other participants. 
    
5. _Optional_: Select an icon and background image to customize how your agent appears in the **Agent Preview** pane.
    
6. Select the AI agent framework you want to use to create, deploy and, manage your agent.
    
    **Note**: Currently, watsonx.ai offers `LangGraph` as the only framework choice.
    
7. Select the architecture that implements agentic AI reasoning.
    
    **Note**: Currently, watsonx.ai offers `ReAct` as the only architecture choice.
    
8. Define specific instructions for your agent that is used to create a system prompt for the selected foundation model. The instructions can include using a specific language, date or time format, user greeting, or an external tool as an information source instead of a foundation model's knowledge base. 
    ```
    You are a helpful assistant that uses tools to answer questions in detail. Answer concisely and clearly. Always answer in Dutch language.
    ```
    
9. In the tools section, make sure **No tools** are enabled by default, remove them if needed.

10.  Now, we're going to try making an LLM call on a new standard without having any access to tools. Try the following prompt in AgentLab without any tools. 

    ```
    Wat zijn de huidige rentetarieven van DNB?
    ```

    ![image](./images/agentlab-2.png)

**Note** that the LLM was trained before this new Code of Practice, and therefor provides an outdated answer. 

### Step 2: Add a `Google search` tool

Now we'll add the Google Tool and try the same prompt:

1. In the **Tools** section, click **Add a tool** and select the **Google search** tool that the agent framework can invoke to compose a response.
    
2. _Optional_: Add some sample questions that the end user can use to start interacting with the agent, like.:

    ```
    Wat zijn de huidige rentetarieven van DNB?
    ```
    
3. Test your agent in the **Agent preview** pane to make sure the agent generates the correct result by using a combination of the foundation model and the relevant tools. You can now ask:

    ```
    Wat zijn de huidige rentetarieven van DNB?
    ```

    ![image](./images/agentlab-3.png)

**Note** that after adding the Google search tool and trying the same prompt, your agent is now referencing the latest changes to the code of practice. In the result, if you click on **How did I get this answer?**, you can get the full trace of your agent's reasoning and actions.

### Step 3: Add a `Webcrawler` tool

What if we wanted to get details from a specific website? Well Billie could use the webscraping tool:

1. In the **Tools** section, click **Add a tool** and select the **Webcrawler** tool that the agent framework can invoke to compose a response.

2. Test your agent in the **Agent preview** pane to make sure the agent generates the correct result by using a combination of the foundation model and the relevant tools. You can now ask:

    ```
        Wat moet ik doen om een gunstige rente te krijgen? Gebruik de volgende website: https://www.nn.nl/Particulier/Hypotheken.htm
    ```

    ![image](./images/agentlab-4.png)

**Note** that now, your agent will summarise the details from that specific website by crawling that page directly.

### Step 4: Ingest documents for Q&A

But Billie needs some more details, what if she had a specific document that she wanted to ground her answers in, rather than using a site what if there was an internal policy:

1. Save your agent in your project by clicking the save Icon on the top, and **Save as**. Select **Agent** and click **Save**.
2. Navigate to your watsonx.ai project, and then click the **New asset > Ground gen AI with vectorized documents** tile.
3. Upload the attached `hypotheek.pdf` document.
4. Name it: `Woordenlijst met hypotheektermen`
5. give it the following description, then click **Create**.
    ```
    Woordenlijst met hypotheektermen
    ```
4. In your project, open your agent in the Agent Lab.
5. In the **Tools** section, click **Add a tool** and select the **Document search** and select the `Woordenlijst met hypotheektermen` vector index that your just created. Click **Select**.
6. Just like that, you've enabled your agent to use RAG and ground some of it's answers in the document, you can test it by asking one of the following:

    ```
    Wat is de drempeldatum?
    ```

    ![image](./images/agentlab-5.png)


**Note** that your agent uses the `RAGQuery` tool to answer your question from the document.

### Step 5: Deploy your Agent

You are now ready to deploy your agent as a new AI service:

1. In the top action bar, click **Deploy**.
2. Select target deployment space: `damen-shipyards-workshop`
    - Alternatively you could [create](https://www.ibm.com/docs/en/watsonx/saas?topic=spaces-creating-deployment) your own deployment space, but we won't do that here, please use the existing one..
3. After a few seconds, your watsonx Agent will be initialized and deployed in the target deployment space.
4. Once deployed, click on your new agent and test it by asking it any of the previous questions in the **Preview** section:

    ![image](./images/agentlab-7.png)

5. **Important:** Required steps which are a prerequisite for the next lab. 
    - For the next Lab, copy and keep streaming public endpoint of your deployed agent. (ends with: `ai_service_stream`). 
    - Create and copy API key. Go to IBM [cloud](https://cloud.ibm.com), in the top menu bar click on **Manage** then on **Access (IAM)**. In the left menubar click on **API keys** and finally create your API key by clicking on the blue **Create** button. 
    - Keep your **streaming public endpoint** and **API Key** for a next Lab.

This concludes the lab exercise.


### Step 6: (Optional) New agent with a Custom Tool

Now let's say that the Bank introduces a new wealth builder fee of `$3000` over the life of the loan which gets added onto monthly payments, how could Billie factor this into her agent? This is where custom tools come in.

1. Go back to your project.
2. Create a new agent.
    - click the **New asset > Build an AI agent to automate tasks** tile.

    ![image](./images/agentlab-1.png)
    - Select a foundation model and optionally update model parameters. Let's use model `llama-3-3-70b-instruct`. For details, see [Foundation model configuration](#model).
    - To set up your agent, specify a name for the agent and describe the tasks the agent performs in the **Setup** section.
        - Set the name to something like `<YOUR-PREFIX>-watsonx-repayment calculator-agent`. Please use e.g. your last name or another unique string within this Lab as a prefix, so that you can distinguish your agent from the agents of other participants.
3. Define specific instructions for your agent that is used to create a system prompt for the selected foundation model. The instructions can include using a specific language, date or time format, user greeting, or an external tool as an information source instead of a foundation model's knowledge base. 
    ```
    You are a helpful assistant that uses tools to answer questions in detail. Answer concisely and clearly. Always answer in Czech language.
    ```
4. In the **Tools** section, click **Create custom tool**.
   1. **Name**: Enter `Termijncalculator`
   2. **Tool description**:
        ```
        Hypotheekrentecalculator. Bereken de maandelijkse hypotheeklasten op basis van het leenbedrag, de rente (percentage) en de looptijd.
        ```
        **Note**: this description is very important, it will be used by the LLM to know when to call this custom tool.
   3. **Input JSON Schema**:
        ```json
        {
        "principal": {
          "title": "Hoofdbedrag van de lening",
          "description": "Totaal leenbedrag",
          "type": "number"
         },
         "interest_rate": {
          "title": "Jaarlijkse rente in procenten",
          "description": "Jaarlijkse rente, d.w.z. decimaal getal in procenten (rentepercentage)",
          "type": "number"
         },
         "period": {
          "title": "Leenperiode",
          "description": "Lengte van de lening in jaren.",
          "type": "integer"
         }
        }
        ```
        **Note**: this schema is very important, it will be used by the LLM to know how to call this tool with the required input parameters.
   4. **Python code**:

        ```py
        def monthly_repayment(principal: float, interest_rate: float, period: int):
            interest_rate = interest_rate / 100
            return (
                principal
                * (interest_rate / 12 * (1 + interest_rate / 12) ** (period * 12))
                / ((1 + interest_rate / 12) ** (period * 12) - 1)
            ) + 3000 / period
        ```

2. Test your agent in the **Agent preview** pane to make sure the agent generates the correct result by using a combination of the foundation model and the relevant tools. You can now ask:

    ```
    Wat zijn de maandelijkse betalingen voor een lening van EUR 248.500 met een rentepercentage van 5,85% gedurende 25 jaar?
    ```

    ![image](./images/agentlab-6.png)

**Note** that your agent is translating your query into a python calculation that he then performs to answer your question.
 
3. You can try to deploy and test the agent. 

## Conclusion

In this hands-on lab, you learned how to build agentic workflows using AgentLab. You created custom tools, used the WebCrawler tool, integrated a Python interpreter, used RAG, and deployed an agent with a custom tool. By applying these skills, you can automate tasks and make informed decisions in your own organization.

## Additional Resources

* watsonx.ai Agents quickstart: [link](https://www.ibm.com/watsonx/developer/agents/quickstart)
* Agent Lab documentation: [link](https://www.ibm.com/docs/en/watsonx/saas?topic=solutions-agent-lab-beta)
* watsonx Developer Hub: [link](https://developer.ibm.com/components/watsonx-ai)
