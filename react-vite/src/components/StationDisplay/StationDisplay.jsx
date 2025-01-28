import { useParams } from "react-router-dom";
import { useContext, useEffect } from "react";
import { GoogleMapContext } from "../../context/GoogleMapContext";
import { useGetSelectedStation } from "../../hooks/useGetSelectedStation";
import "./StationDisplay.css";
import StationImageDisplay from "./StationDataComponents/StationImageDisplay";
import PriceOptionsDisplay from "./StationDataComponents/PriceOptionsDisplay";
import ReviewsDisplay from "./StationDataComponents/ReviewsDisplay";
import { AdvancedMarker, Map } from "@vis.gl/react-google-maps";

function StationDisplay() {
  const { id } = useParams();
  const stationInfo = useGetSelectedStation(id);


  const mapId = import.meta.env.VITE_REACT_APP_GOOGLE_MAP_ID_LIGHT_MODE


  const { setSelectedStation } = useContext(GoogleMapContext);

  useEffect(() => {
    if (stationInfo) {
      setSelectedStation(stationInfo);
    }
  }, [stationInfo, setSelectedStation]);


  if (!stationInfo) return <h1>Loading...</h1>;
  const center = {
    lat: stationInfo.location.latitude,
    lng: stationInfo.location.longitude,
  };

  return (
    <section className={`station-display-main-container-light`}>
      <div className="image-scroll-track">
        {stationInfo.photos && <StationImageDisplay />}
      </div>
      <div className="station-data-container">
        <h1>{stationInfo.displayName.text}</h1>
        <p>{stationInfo.formattedAddress}</p>
        <PriceOptionsDisplay stationInfo={stationInfo} />
        <div className="review-map-container">
          <ReviewsDisplay
            stationInfo={stationInfo}
            onReviewAdded={console.log}
            onPriceAdded={console.log}
          />
          <Map
            center={center}
            style={{
              width: "100%",
              height: "100%",
              minHeight: "32rem",
            }}
            mapId={mapId}
            zoom={18}
            disableDefaultUI={true}
            gestureHandling={"greedy"}
          >
            <AdvancedMarker position={center} />
          </Map>
        </div>
      </div>
    </section>
  );
}

export default StationDisplay;
