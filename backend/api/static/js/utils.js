async function apiFetch(url, method="GET", body=null,headers={}){
    try {
        const config = {
            method,
            headers:{
                "Content-Type": 'application/json',
                ...headers
            },

        };
        if(body){
            config.body = JSON.stringify(body)
        }
        const resposta = await fetch(url,config)
        
        return await resposta.json()
    } catch (error) {
        
    }
}

alert("passou aqui viado")