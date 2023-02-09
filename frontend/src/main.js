import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'
import { createVuestic } from 'vuestic-ui'
import 'vuestic-ui/css'

createApp(App).use(
    createVuestic({
        config: {
            colors: {
                variables: {
                    primary: '#41729F',
                    secondary: '#5885AF',
                    backgroundPrimary: '#274472',
                    backgroundSecondary: '#C3E0E5',
                    success: '#40e583',
                    info: '#2c82e0',
                    danger: '#e34b4a',
                    warning: '#ffc200',
                    gray: '#babfc2',
                    dark: '#34495e',
                }
            }
        }
    })).mount('#app')
