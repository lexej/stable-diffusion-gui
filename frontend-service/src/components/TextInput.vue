<template>
    <div class="column2">
        <div class="container-inside">
          <div class="conversation-history">

            <div v-if="this.generated_image !== null">
              <div>{{ this.promptAnswer }}</div>
              <div class="m-2">
                <img v-bind:src="'data:image/jpeg;base64,'+this.generated_image['image_string']" alt="Red dot"/>
              </div>
            </div>

            <div v-if="this.generated_image === null">
              <div v-if="isGeneratingImage">
                <div class="loading-container">
                  <div class="loader"></div>
                </div>
              </div>
              <div v-else>
                <div class="center-container">Enter prompt and negative prompt to create image</div>
              </div>
            </div>
                  
          </div>

          <div class="input-container">
            <input v-model="promptInput" class="prompt-field" type="text" placeholder="Enter the prompt" :disabled="isGeneratingImage" @keydown.enter.prevent="handleEnter" />
              <input v-model="negativePromptInput" class="negative_prompt_field" type="text" placeholder="Enter the negative prompt" :disabled="isGeneratingImage" @keydown.enter.prevent="handleEnter" />
              <button @click="handleEnter" :disabled="isGeneratingImage" :class="{ 'disabled-button': isGeneratingImage }">Generate image</button>
          </div>
        </div>
    </div>
</template>
  
 <script>
import axios from 'axios'

  export default {
    data() {
      return {
        promptInput: "",
        negativePromptInput: "",
        promptAnswer: "",
        generated_image: null,
        isGeneratingImage: false,
      };
    },
    computed: {
    },
    methods: {
      disableInput(){
        this.isGeneratingImage = true;
      },
      prepareForInput(){
        this.isGeneratingImage = false;
        this.promptInput = "";
        this.negativePromptInput = "";
      },
      handleEnter() {
        this.disableInput();

        this.generated_image = null;

        this.promptAnswer = `Your generated image for prompt "${this.promptInput}" and negative prompt "${this.negativePromptInput}":`

        const userPrompt = {prompt: this.promptInput, negative_prompt: this.negativePromptInput};
        
        this.getImageString(userPrompt);
        
      },
      getImageString(userPrompt) {
        
        axios.post("/api/image/", userPrompt).then((response) =>  {
          this.generated_image = response.data;
          this.prepareForInput();
        });
      },
    },
  };
</script>
  
<style scoped>
.disabled-button {
    opacity: 0.5;
    cursor: not-allowed;
}
.prompt-field{
  background-color: rgba(51, 170, 51, .1);
}
.negative_prompt_field{
  background-color: rgba(250,128,114, .1);
}

img {
  margin: 1.8em;
  width: auto; 
  height: 55vh;
  max-width: 100%;
  max-height: 100%;
}
.container-inside {
    text-align: center;
    width: 100%;
    height: 80vh;
}
.conversation-history {
    flex: 4;
    border: 0.5px solid #0056b3;
    padding: 10px;
    margin-bottom: 10px;
    height: 70vh;
    overflow-y: auto;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    position: relative;
}

.center-container {
  font-size: 1.4em;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
}

.input-container {
  flex: 1;
  width: 100%;
  max-width: 100%;
  display: flex;
}

input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0056b3;
}


.loading-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.loader {
  border: 8px solid #f3f3f3;
  border-top: 8px solid #3498db;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
  