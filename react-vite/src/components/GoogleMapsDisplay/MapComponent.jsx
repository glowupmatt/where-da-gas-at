import { Map, AdvancedMarker } from "@vis.gl/react-google-maps";
import { useEffect, useState, useContext } from "react";
import { GoogleMapContext } from "../../context/GoogleMapContext";
import { useSelector } from "react-redux";
import "./MapComponent.css";
import GoogleMapsNearByLocations from "./GoogleMapsNearByLocations";
import InfoWindowComponent from "./InfoWindowComponent";

function MapComponent() {
  const {
    center,
    newCenter,
    setNewCenter,
    nearbyStations,
    selectedStation,
    map,
    zoom,
    setSelectedStation,
    setZoom,
  } = useContext(GoogleMapContext);

  const [stations, setStations] = useState([])
  const sessionUser = useSelector((state) => state.session.user);

  //This useEffect will run when the map and newCenter is available
  useEffect(() => {
    if (map && newCenter) {
      map.setCenter(newCenter);
    }
  }, [map, newCenter, center]);

  const handleDragEnd = () => {
    if (map) {
      const newCenter = map.getCenter();
      setNewCenter({ lat: newCenter.lat(), lng: newCenter.lng() });
    }
  };

  useEffect(() => {
    if (sessionUser.errors) return;

    const fetchStations = async () => {
      try {
        const res = await fetch("/api/station/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();
        setStations(Object.values(data.station));
      } catch (error) {
        console.error("Failed to fetch stations:", error);
      }
    };
    fetchStations()
  }, [sessionUser]);

  useEffect(() => {
    if (sessionUser.errors) return;

    const postStation = async (station) => {
      const body = {
        id: station.id,
        name: station.displayName.text,
        lat: station.location.latitude,
        lng: station.location.longitude,
        address: station.formattedAddress,
        uri: station.googleMapsUri,
      };

      try {
        const res = await fetch("/api/station/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(body),
        });

        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();
        console.log("Station saved successfully:", data);
      } catch (error) {
        console.error("Failed to post station:", error);
      }
    };

    const postUnsavedStations = async () => {
      const existingStationIds = stations.map(station => station.id);
      console.log("Existing station IDs:", existingStationIds);
      const unsavedStations = (nearbyStations).filter(
        station => !existingStationIds.includes(station.id)
      );

      console.log("Unsaved stations:", unsavedStations);
      for (const station of unsavedStations) {
        await postStation(station);
      }
    };

    postUnsavedStations();
  }, [nearbyStations, sessionUser, stations]);



  return (
    //This is the main map rendered on the screen. There are a lot of
    //prebuilt props that can be used to customize the map.
    <Map
      // onLoad={onLoad}
      onDragend={handleDragEnd}
      style={{ width: "100%", height: "100vh" }}
      defaultCenter={center}
      mapId={
        import.meta.env.VITE_REACT_APP_GOOGLE_MAP_ID ||
        "e2ea39204ffcffc4"
      }
      defaultZoom={15}
      zoom={zoom}
      onZoomChanged={() => setZoom(map.getZoom())}
      onClick={() => selectedStation && setSelectedStation(null)}
      disableDefaultUI={true}
      gestureHandling={"greedy"}
    >
      <AdvancedMarker position={center}>
        <div>
          <img
            className="user-marker"
            src="/user.svg"
            width={32}
            height={32}
          />
        </div>
      </AdvancedMarker>
      {/* Here we conditionally render the Info Window Component. If a
       * user selects a station the it will appear */}
      {selectedStation && <InfoWindowComponent />}
      {/* This is the component that will render all the nearby
       * station markers on the map */}
      <GoogleMapsNearByLocations nearbyStations={nearbyStations} />
    </Map>
  );
}

export default MapComponent;
