module ("templates.SmartHomeTemplate", thingworx.template.extend)

properties.LED={baseType="BOOLEAN", pushType="ALWAYS", value=0}
properties.Lock={baseType="BOOLEAN", pushType="ALWAYS", value=0}
properties.Timestamp={baseType="STRING", pushType="ALWAYS", value=0}

serviceDefinitions.UpdateLedandLock(
    output { baseType="BOOLEAN", description="" },
    description { "updates properties" }
)

serviceDefinitions.ToggleLock(
    output { baseType="BOOLEAN", description="" },
    description { "updates properties" }
)

serviceDefinitions.ToggleLED(
    output { baseType="BOOLEAN", description="" },
    description { "updates properties" }
)

serviceDefinitions.CaptureImage(
    output { baseType="BOOLEAN", description="" },
    description { "updates properties" }
)

services.ToggleLock = function(me, headers, query, data)
log.trace("[PiTemplate]","########### in ToggleLock #############")
ServoToggle()
return 200, true
end

services.ToggleLED = function(me, headers, query, data)
log.trace("[PiTemplate]","########### in ToggleLED #############")
LedToggle()
return 200, true
end

services.CaptureImage = function(me, headers, query, data)
log.trace("[PiTemplate]","########### in CaptureImage #############")
local f = io.popen("python /home/pi/Desktop/Camera.py")
properties.Timestamp.value = f:read("*a")
return 200, true
end

services.UpdateLedandLock = function(me, headers, query, data)
log.trace("[PiTemplate]","########### in UpdateLedandLock#############")
-- querySensor()
return 200, true
end

function LedToggle()
querySensor()
if properties.LED.value == false then
    io.popen("python /home/pi/Desktop/LedOn.py")  
    properties.LED.value = true

elseif properties.LED.value == true then
    io.popen("python /home/pi/Desktop/LedOff.py")
    properties.LED.value = false
end

end

function ServoToggle()
querySensor()
if properties.Lock.value == false then
    io.popen("python /home/pi/Desktop/DoorOpen.py") 
    properties.Lock.value = true  
    
elseif properties.Lock.value == true then
    io.popen("python /home/pi/Desktop/DoorClose.py")
    properties.Lock.value = false
end

end


function querySensor()
local f = io.popen("python /home/pi/Desktop/RefreshLedLock.py")
local s = f:read("*a")

if s == '1' then
properties.LED.value = false 
properties.Lock.value = false

elseif s == '2' then
properties.LED.value = true 
properties.Lock.value = false

elseif s == '3' then
properties.LED.value = false 
properties.Lock.value = true

elseif s == '4' then
properties.LED.value = true
properties.Lock.value = true
end

end

tasks.refreshProperties = function(me)
log.trace("[PiTemplate]","~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ In tasks.refreshProperties~~~~~~~~~~~~~ ")
querySensor()
end

