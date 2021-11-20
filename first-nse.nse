
-- HEAD

description = [[
Simple script that determines if a TCP port is open.
]]

author = "Bill Kachersky"

-- RULE

portrule = function(host, port)
        return port.protocol == "tcp"
                and port.state == "open"
end

-- ACTION
-- IF PORT IS OPEN, MESSAGE DISPLAYS

action = function(host, port)
        return "This is LAB not an OPS CHALLENGE!"
end


