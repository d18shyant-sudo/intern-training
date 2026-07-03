interface prop{
    title:string;
    description:string;
}
function Card(props:prop){
    return (
        <div>
            <h2>{props.title}</h2>
            <h2>{props.description}</h2>
            <br></br>
        </div>
    )
}
export default Card;