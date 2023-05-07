<template>
    <div dark class="card">
        <div class="card_head">
            <div class="card_dots">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        </div>
        <v-divider dark></v-divider>
        <div class="card_body">
                <code class="code_head">{{resh1}}</code>
                <br/>
                <code class="code_body">
                    {{resb1}}
                </code>
                <br/>
                <br/>
                <code class="code_head">{{resh2}}</code>
                <br/>
                <code class="code_body">
                    {{resb2}}
                </code>
                <br/>
                <br/>
                <code class="code_head">{{resh3}}</code>
                <br/>
                <code class="code_body">
                    {{resb3}}
                </code>
                <br/>
                <code class="code_body">
                    {{resb4}}
                </code>
                <br/>
                <code class="code_body">
                    {{resb5}}
                </code>
                
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return({
            head1: '> $ ФИСТ УлГТУ. Курсы Северной долины ',
            resh1: '',
            head2: '> $ npm install ',
            resh2: '',
            head3: '> $ npm start',
            resh3: '',
            body1: 'Верный шаг в смене профессии!',
            resb1: '',
            body2: 'Everything is installed',
            resb2: '',
            body3: 'scss watching',
            resb3: '',
            body4: 'LiveReload started',
            resb4: '',
            body5: 'Opening localhost:8080',
            resb5: ''
        })
    },
    mounted() {
        this.makeTxt()
    },
    methods: {
        c_head1(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.head1.slice(0, len)
                    len++
                    this.resh1 = res
                    if (this.resh1 == this.head1) {
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_body1(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.body1.slice(0, len)
                    len++
                    this.resb1 = res
                    if (this.resb1 == this.body1) {
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_head2(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.head2.slice(0, len)
                    len++
                    this.resh2 = res
                    if (this.resh2 == this.head2) {
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_body2(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.body2.slice(0, len)
                    len++
                    this.resb2 = res
                    if (this.resb2 == this.body2){
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_head3(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.head3.slice(0, len)
                    len++
                    this.resh3 = res
                    if (this.resh3 == this.head3){
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_body3(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.body3.slice(0, len)
                    len++
                    this.resb3 = res
                    if (this.resb3 == this.body3){
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_body4(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.body4.slice(0, len)
                    len++
                    this.resb4 = res
                    if (this.resb4 == this.body4){
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        c_body5(){
            let res = ''
            let len = 0
            return new Promise((resolve, reject)=>{
                let k = setInterval(()=>{
                    res=this.body5.slice(0, len)
                    len++
                    this.resb5 = res
                    if (this.resb5 == this.body5){
                        resolve(true) 
                        clearInterval(k)
                    }
                },40)
            })
        },
        makeTxt(){
            this.c_head1()
            .then(()=>this.c_body1()
                .then(()=>this.c_head2()
                    .then(()=>this.c_body2()
                        .then(()=>this.c_head3()
                            .then(()=>this.c_body3()
                                .then(()=>this.c_body4()
                                    .then(()=>this.c_body5()
                                        .then(()=>{
                                            setTimeout(()=>{
                                                let deleteCount = 0
                                                let t = setInterval(()=>{
                                                    deleteCount++
                                                    this.resh1=this.resh1.slice(0,this.resh1.length-deleteCount)
                                                    this.resh2=this.resh2.slice(0,this.resh2.length-deleteCount)
                                                    this.resh3=this.resh3.slice(0,this.resh3.length-deleteCount)
                                                    this.resb1=this.resb1.slice(0,this.resb1.length-deleteCount)
                                                    this.resb2=this.resb2.slice(0,this.resb2.length-deleteCount)
                                                    this.resb3=this.resb3.slice(0,this.resb3.length-deleteCount)
                                                    this.resb4=this.resb4.slice(0,this.resb4.length-deleteCount)
                                                    this.resb5=this.resb5.slice(0,this.resb5.length-deleteCount)
                                                    if(this.resh1==''){
                                                        clearInterval(t)
                                                        this.makeTxt()
                                                    }
                                                }, 100)
                                            }, 700)
                                            
                                        
                                            
                                        }
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        }
    }

}
</script>


<style lang="scss" scoped>
    .card{
        color: #c4c4c4;
        border-radius: 16px;
        background-color: #161c2d; 
        .code_body{
            color: #42ba96
        }
    }
    .card_head{
        padding: 20px 35px
        
    }
    .card_body{
        padding: 30px 40px
    }
    .card_dots{
        display: flex;
    
        .dot{
            width: 12px;
            height: 12px;
            margin-right: 4px;
            background-color: #df4759;
            border-radius: 50%
        }
        :nth-child(2){
            background-color: #fad776
        }
        :nth-child(3){
            background-color: #42ba96;
        }
    }


    
    
</style>
